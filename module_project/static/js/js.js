document.addEventListener('DOMContentLoaded', () => {

    // ===================== Drag & Drop =====================
    const dragItems = document.querySelectorAll('.drag-item');
    const dropZones = document.querySelectorAll('.drop-zone');

    dragItems.forEach(item => {
        item.addEventListener('dragstart', (e) => {
            e.dataTransfer.setData("id", item.dataset.id);
            e.dataTransfer.setData("type", item.dataset.type);
            e.dataTransfer.setData("name", item.innerText.trim());
        });
    });

    dropZones.forEach(zone => {
        const acceptedType = zone.dataset.acceptedType;
        const nameDisplay = document.getElementById(acceptedType + '-name');

        zone.addEventListener('dragover', (e) => {
            e.preventDefault();
            zone.classList.add('over');
        });

        zone.addEventListener('dragleave', () => {
            zone.classList.remove('over');
        });

        zone.addEventListener('drop', (e) => {
            e.preventDefault();
            zone.classList.remove('over');

            const draggedType = e.dataTransfer.getData("type");
            const id = e.dataTransfer.getData("id");
            const name = e.dataTransfer.getData("name");

            if (draggedType === acceptedType) {
                // Правильный тип — зелёный
                document.getElementById(acceptedType + '_id').value = id;
                nameDisplay.innerHTML = `<strong>${name}</strong>`;
                zone.style.borderColor = '#22c55e';
                zone.style.backgroundColor = 'rgba(34, 197, 94, 0.15)';
            } else {
                // Неправильный тип — красный
                zone.style.borderColor = '#ef4444';
                zone.style.backgroundColor = 'rgba(239, 68, 68, 0.2)';
                nameDisplay.innerHTML = '<span style="color:#ef4444;">⛔ Неверный тип!</span>';

                setTimeout(() => {
                    zone.style.borderColor = '#64748b';
                    zone.style.backgroundColor = 'rgba(0,0,0,0.2)';
                    nameDisplay.innerHTML = '';
                }, 1600);
            }
        });
    });

    // ===================== Вкладки =====================
    const tabs = document.querySelectorAll('.tab');
    const elementFilter = document.getElementById('element-filter');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            // Переключаем активную вкладку
            tabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');

            // Переключаем содержимое
            document.querySelectorAll('.tab-content').forEach(content => {
                content.classList.remove('active');
            });
            document.getElementById('tab' + tab.dataset.tab).classList.add('active');

            // Фильтр показываем ТОЛЬКО на вкладке Персонажи
            if (tab.dataset.tab === '0') {
                elementFilter.classList.add('visible');
            } else {
                elementFilter.classList.remove('visible');
            }
        });
    });

    // ===================== Фильтр по элементам =====================
    const filterBtns = document.querySelectorAll('.filter-btn');
    const characterItems = document.querySelectorAll('.character-item');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const selectedElement = btn.dataset.element;

            characterItems.forEach(item => {
                if (selectedElement === 'all') {
                    item.style.display = 'block';
                } else {
                    item.style.display =
                        (item.dataset.element === selectedElement) ? 'block' : 'none';
                }
            });
        });
    });

        const scroll = document.querySelector('.builds-scroll');
    const btnLeft = document.getElementById('scroll-left');
    const btnRight = document.getElementById('scroll-right');

    if (!scroll || !btnLeft || !btnRight) return;

    // Ширина одной карточки + gap
    function getCardWidth() {
        const card = scroll.querySelector('.build-card');
        if (!card) return 300;
        const style = window.getComputedStyle(scroll);
        const gap = parseFloat(style.gap) || 24;
        return card.offsetWidth + gap;
    }

    // Листаем вправо
    btnRight.addEventListener('click', () => {
        const cardWidth = getCardWidth();
        const maxScroll = scroll.scrollWidth - scroll.clientWidth;

        if (scroll.scrollLeft >= maxScroll - 5) {
            // Дошли до конца — возвращаемся в начало (цикл)
            scroll.scrollTo({ left: 0, behavior: 'smooth' });
        } else {
            scroll.scrollBy({ left: cardWidth, behavior: 'smooth' });
        }
    });

    // Листаем влево
    btnLeft.addEventListener('click', () => {
        const cardWidth = getCardWidth();

        if (scroll.scrollLeft <= 5) {
            // Дошли до начала — переходим в конец (цикл)
            scroll.scrollTo({ left: scroll.scrollWidth, behavior: 'smooth' });
        } else {
            scroll.scrollBy({ left: -cardWidth, behavior: 'smooth' });
        }
    });
});