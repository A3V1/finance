from flask import Blueprint, render_template, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from app import db
from app.forms import FinancialDataForm
from app.models import Income, Expense, Saving, Investment
from app.ml import generate_recommendations, predict_future_expenses, check_alerts
from sqlalchemy import func

views = Blueprint('views', __name__)


@views.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = FinancialDataForm()
    
    if form.validate_on_submit():
        try:
            income = Income(amount=form.income.data, user_id=current_user.id)
            expense = Expense(amount=form.expenses.data, user_id=current_user.id)
            saving = Saving(amount=form.savings.data, user_id=current_user.id)
            investment = Investment(amount=form.investments.data, user_id=current_user.id)
            
            db.session.add_all([income, expense, saving, investment])
            db.session.commit()
            
            flash('Financial data submitted successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred: {str(e)}', 'danger')
        return redirect(url_for('views.dashboard'))

    # Fetch financial data for the current user
    income = db.session.query(func.sum(Income.amount)).filter_by(user_id=current_user.id).scalar() or 0
    expenses = db.session.query(func.sum(Expense.amount)).filter_by(user_id=current_user.id).scalar() or 0
    savings = db.session.query(func.sum(Saving.amount)).filter_by(user_id=current_user.id).scalar() or 0
    investments = db.session.query(func.sum(Investment.amount)).filter_by(user_id=current_user.id).scalar() or 0

    # Fetch AI/ML results
    recommendation = generate_recommendations(current_user.id)
    prediction = predict_future_expenses(current_user.id)
    alert = check_alerts(current_user.id)
    
    return render_template('dashboard.html', form=form, recommendation=recommendation, prediction=prediction, alert=alert,
                           income=income, expenses=expenses, savings=savings, investments=investments)

@views.route('/api/financial_data')
@login_required
def get_financial_data():
    income = db.session.query(func.sum(Income.amount)).filter_by(user_id=current_user.id).scalar() or 0
    expenses = db.session.query(func.sum(Expense.amount)).filter_by(user_id=current_user.id).scalar() or 0
    savings = db.session.query(func.sum(Saving.amount)).filter_by(user_id=current_user.id).scalar() or 0
    investments = db.session.query(func.sum(Investment.amount)).filter_by(user_id=current_user.id).scalar() or 0
    
    return jsonify({
        'income': income,
        'expenses': expenses,
        'savings': savings,
        'investments': investments
    })