document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/financial_data')
        .then(response => response.json())
        .then(data => {
            var ctx = document.getElementById('financialChart').getContext('2d');
            var financialChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ['Income', 'Expenses', 'Savings', 'Investments'],
                    datasets: [{
                        label: 'Financial Data',
                        data: [data.income, data.expenses, data.savings, data.investments],
                        backgroundColor: [
                            'rgba(75, 192, 192, 0.2)',
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(54, 162, 235, 0.2)',
                            'rgba(255, 206, 86, 0.2)'
                        ],
                        borderColor: [
                            'rgba(75, 192, 192, 1)',
                            'rgba(255, 99, 132, 1)',
                            'rgba(54, 162, 235, 1)',
                            'rgba(255, 206, 86, 1)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        });
});