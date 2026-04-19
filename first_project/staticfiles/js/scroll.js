document.addEventListener('DOMContentLoaded', () => {
    const scrollContainer = document.querySelector('.builds-scroll');
    const btnLeft = document.getElementById('scroll-left');
    const btnRight = document.getElementById('scroll-right');

    if (!scrollContainer || !btnLeft || !btnRight) return;

    const scrollAmount = 320; // примерно ширина одной карточки + отступ

    // Прокрутка вправо
    btnRight.addEventListener('click', () => {
        scrollContainer.scrollBy({
            left: scrollAmount,
            behavior: 'smooth'
        });
    });

    // Прокрутка влево
    btnLeft.addEventListener('click', () => {
        scrollContainer.scrollBy({
            left: -scrollAmount,
            behavior: 'smooth'
        });
    });

    // Показывать/скрывать кнопки в зависимости от позиции скролла
    function updateButtons() {
        const maxScroll = scrollContainer.scrollWidth - scrollContainer.clientWidth;
        
        btnLeft.style.opacity = scrollContainer.scrollLeft > 20 ? '1' : '0.3';
        btnRight.style.opacity = scrollContainer.scrollLeft < maxScroll - 20 ? '1' : '0.3';
    }

    scrollContainer.addEventListener('scroll', updateButtons);
    window.addEventListener('resize', updateButtons);
    
    // Первоначальная проверка
    setTimeout(updateButtons, 300);
});