// JavaScript logic for Mishka's Interactive Web Ebook

document.addEventListener('DOMContentLoaded', () => {
    let currentPage = 1;
    const totalPages = 15; // Cover (1), Pages 1-13 (2-14), Back Cover (15)

    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    const pageNumDisplay = document.getElementById('pageNumDisplay');
    const tocBtn = document.getElementById('tocBtn');
    const tocDrawer = document.getElementById('tocDrawer');
    const readAloudBtn = document.getElementById('readAloudBtn');

    // Page updates
    function updatePage(newPage) {
        if (newPage < 1 || newPage > totalPages) return;
        
        // Hide previous page
        const activePage = document.querySelector('.page-content.active');
        if (activePage) {
            activePage.classList.remove('active');
        }

        // Stop speech if playing
        if (window.speechSynthesis) {
            window.speechSynthesis.cancel();
        }

        currentPage = newPage;
        const targetPage = document.getElementById(`page-${currentPage}`);
        if (targetPage) {
            targetPage.classList.add('active');
        }

        // Update Nav UI
        prevBtn.disabled = (currentPage === 1);
        nextBtn.disabled = (currentPage === totalPages);

        if (currentPage === 1) {
            pageNumDisplay.textContent = 'Cover';
        } else if (currentPage === totalPages) {
            pageNumDisplay.textContent = 'Back Cover';
        } else {
            pageNumDisplay.textContent = `Page ${currentPage - 1} of 13`;
        }

        // Scroll page top
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // Nav Listeners
    prevBtn.addEventListener('click', () => updatePage(currentPage - 1));
    nextBtn.addEventListener('click', () => updatePage(currentPage + 1));

    // Keyboard Navigation
    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowLeft') updatePage(currentPage - 1);
        if (e.key === 'ArrowRight') updatePage(currentPage + 1);
    });

    // TOC Drawer Toggle
    tocBtn.addEventListener('click', () => {
        tocDrawer.classList.toggle('active');
    });

    // TOC Items Click
    document.querySelectorAll('.toc-item').forEach(item => {
        item.addEventListener('click', () => {
            const pageIndex = parseInt(item.getAttribute('data-page'), 10);
            updatePage(pageIndex);
            tocDrawer.classList.remove('active');
        });
    });

    // Close TOC if clicked outside
    document.addEventListener('click', (e) => {
        if (!tocDrawer.contains(e.target) && !tocBtn.contains(e.target)) {
            tocDrawer.classList.remove('active');
        }
    });

    // Interactive Flaps & Tabs Listeners
    document.querySelectorAll('.interactive-badge, .interactive-flap-container, .interactive-tab-container, .interactive-envelope-container').forEach(elem => {
        elem.addEventListener('click', () => {
            if (elem.classList.contains('open') || elem.classList.contains('pulled')) {
                elem.classList.remove('open', 'pulled');
            } else {
                elem.classList.add('open', 'pulled');
            }
        });
    });

    // Read Aloud Feature (Web Speech API)
    if ('speechSynthesis' in window) {
        readAloudBtn.addEventListener('click', () => {
            if (window.speechSynthesis.speaking) {
                window.speechSynthesis.cancel();
                readAloudBtn.innerHTML = '🔊 Read Aloud';
                return;
            }

            const activePage = document.querySelector('.page-content.active');
            if (!activePage) return;

            const textToRead = activePage.querySelector('.story-bubble')?.textContent || activePage.querySelector('.page-title')?.textContent;
            if (!textToRead) return;

            const utterance = new SpeechSynthesisUtterance(textToRead);
            utterance.rate = 0.9; // Slightly slower for clear storytelling
            utterance.pitch = 1.1;

            utterance.onstart = () => {
                readAloudBtn.innerHTML = '⏸️ Pause Narration';
            };

            utterance.onend = () => {
                readAloudBtn.innerHTML = '🔊 Read Aloud';
            };

            window.speechSynthesis.speak(utterance);
        });
    } else {
        readAloudBtn.style.display = 'none';
    }

    // Initialize Page 1
    updatePage(1);
});
