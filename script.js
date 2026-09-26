// JavaScript logic for Mishka's Interactive Web Ebook - Publisher Edition

document.addEventListener('DOMContentLoaded', () => {
    let currentPage = 1;
    const totalPages = 15; // Front Cover (1), Pages 1-13 (2-14), Back Cover (15)

    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const pageNumDisplay = document.getElementById('pageNumDisplay');
    const tocBtn = document.getElementById('tocBtn');
    const tocDrawer = document.getElementById('tocDrawer');
    const readAloudBtn = document.getElementById('readAloudBtn');
    const toggleOriginalsBtn = document.getElementById('toggleOriginalsBtn');

    function updatePage(newPage) {
        if (newPage < 1 || newPage > totalPages) return;

        const activePage = document.querySelector('.page-content.active');
        if (activePage) {
            activePage.classList.remove('active');
        }

        if (window.speechSynthesis) {
            window.speechSynthesis.cancel();
            if (readAloudBtn) readAloudBtn.innerHTML = '🔊 Read Aloud';
        }

        currentPage = newPage;
        const targetPage = document.getElementById(`page-${currentPage}`);
        if (targetPage) {
            targetPage.classList.add('active');
        }

        prevBtn.disabled = (currentPage === 1);
        nextBtn.disabled = (currentPage === totalPages);

        if (currentPage === 1) {
            pageNumDisplay.textContent = 'Front Cover';
        } else if (currentPage === totalPages) {
            pageNumDisplay.textContent = 'Back Cover — About the Book';
        } else {
            pageNumDisplay.textContent = `Page ${currentPage - 1} of 13`;
        }

        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    prevBtn.addEventListener('click', () => updatePage(currentPage - 1));
    nextBtn.addEventListener('click', () => updatePage(currentPage + 1));

    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowLeft') updatePage(currentPage - 1);
        if (e.key === 'ArrowRight') updatePage(currentPage + 1);
    });

    tocBtn.addEventListener('click', () => {
        tocDrawer.classList.toggle('active');
    });

    document.querySelectorAll('.toc-item').forEach(item => {
        item.addEventListener('click', () => {
            const pageIndex = parseInt(item.getAttribute('data-page'), 10);
            updatePage(pageIndex);
            tocDrawer.classList.remove('active');
        });
    });

    document.addEventListener('click', (e) => {
        if (!tocDrawer.contains(e.target) && !tocBtn.contains(e.target)) {
            tocDrawer.classList.remove('active');
        }
    });

    if (toggleOriginalsBtn) {
        toggleOriginalsBtn.addEventListener('click', () => {
            document.body.classList.toggle('show-originals');
            const showing = document.body.classList.contains('show-originals');
            toggleOriginalsBtn.innerHTML = showing
                ? '✨ Hide Original Drawings'
                : '🖼️ Compare Original Drawings';
        });
    }

    if ('speechSynthesis' in window && readAloudBtn) {
        readAloudBtn.addEventListener('click', () => {
            if (window.speechSynthesis.speaking) {
                window.speechSynthesis.cancel();
                readAloudBtn.innerHTML = '🔊 Read Aloud';
                return;
            }

            const activePage = document.querySelector('.page-content.active');
            if (!activePage) return;

            const textToRead = activePage.querySelector('.story-bubble')?.textContent
                || activePage.querySelector('.about-book-card p')?.textContent
                || activePage.querySelector('.page-title')?.textContent;
            if (!textToRead) return;

            const utterance = new SpeechSynthesisUtterance(textToRead.trim());
            utterance.rate = 0.92;
            utterance.pitch = 1.05;

            utterance.onstart = () => {
                readAloudBtn.innerHTML = '⏸️ Stop Reading';
            };

            utterance.onend = () => {
                readAloudBtn.innerHTML = '🔊 Read Aloud';
            };

            window.speechSynthesis.speak(utterance);
        });
    }

    updatePage(1);
});
