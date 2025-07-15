document.addEventListener('DOMContentLoaded', function() {
    // Transaction filtering
    const filterForm = document.getElementById('filter-form');
    if (filterForm) {
        filterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const type = this.elements['type'].value;
            const startDate = this.elements['start_date'].value;
            const endDate = this.elements['end_date'].value;
            
            
            alert(`Filtering by: Type=${type || 'All'}, Start=${startDate || 'None'}, End=${endDate || 'None'}`);
        });
    }
    
    // animation on balance display
    const balanceElements = document.querySelectorAll('.balance-amount');
    balanceElements.forEach(el => {
        const target = parseFloat(el.textContent.replace('$', ''));
        let current = 0;
        const increment = target / 30;
        
        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }
            el.textContent = '$' + current.toFixed(2);
        }, 30);
    });
    
    // Password strength shower
    const passwordInputs = document.querySelectorAll('input[type="password"]');
    passwordInputs.forEach(input => {
        input.addEventListener('input', function() {
            const strengthIndicator = this.nextElementSibling;
            if (strengthIndicator && strengthIndicator.tagName === 'SMALL') {
                const strength = calculatePasswordStrength(this.value);
                strengthIndicator.textContent = `Password strength: ${strength}`;
                strengthIndicator.style.color = getStrengthColor(strength);
            }
        });
    });
    
    function calculatePasswordStrength(password) {
        let strength = 0;
        if (password.length >= 8) strength++;
        if (password.length >= 12) strength++;
        if (/[A-Z]/.test(password)) strength++;
        if (/[0-9]/.test(password)) strength++;
        if (/[^A-Za-z0-9]/.test(password)) strength++;
        
        const ratings = ['Very Weak', 'Weak', 'Moderate', 'Strong', 'Very Strong'];
        return ratings[Math.min(strength, ratings.length - 1)];
    }
    
    function getStrengthColor(strength) {
        const colors = {
            'Very Weak': 'red',
            'Weak': 'orange',
            'Moderate': 'yellow',
            'Strong': 'lightgreen',
            'Very Strong': 'green'
        };
        return colors[strength] || 'black';
    }
});