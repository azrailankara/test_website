// Sayfa yüklendiğinde tema tercihini kontrol et
document.addEventListener('DOMContentLoaded', function() {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        if (savedTheme === 'light') {
            document.body.classList.remove('dark-mode');
            document.getElementById('darkModeIcon').textContent = '🌙';
        } else {
            document.body.classList.add('dark-mode');
            document.getElementById('darkModeIcon').textContent = '☀️';
        }
    }
});

function toggleDarkMode() {
    const body = document.body;
    const icon = document.getElementById('darkModeIcon');
    
    if (body.classList.contains('dark-mode')) {
        body.classList.remove('dark-mode');
        icon.textContent = '🌙';
        localStorage.setItem('theme', 'light');
    } else {
        body.classList.add('dark-mode');
        icon.textContent = '☀️';
        localStorage.setItem('theme', 'dark');
    }
} 