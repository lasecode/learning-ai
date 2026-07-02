document.addEventListener('DOMContentLoaded', () => {
    // 1. Instant card filtering on search input
    const searchInput = document.querySelector('.search-input');
    const contactCards = document.querySelectorAll('.contacts-grid > .contact-card-wrapper');
    const emptyState = document.querySelector('.empty-state');

    if (searchInput && contactCards.length > 0) {
        searchInput.addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase().trim();
            let visibleCount = 0;

            contactCards.forEach(cardWrapper => {
                const name = cardWrapper.getAttribute('data-name').toLowerCase();
                const email = cardWrapper.getAttribute('data-email').toLowerCase();
                const phone = cardWrapper.getAttribute('data-phone').toLowerCase();

                if (name.includes(query) || email.includes(query) || phone.includes(query)) {
                    cardWrapper.style.display = 'block';
                    cardWrapper.style.opacity = '1';
                    visibleCount++;
                } else {
                    cardWrapper.style.display = 'none';
                    cardWrapper.style.opacity = '0';
                }
            });

            // Handle dynamic empty state
            if (visibleCount === 0) {
                if (!document.querySelector('.no-results-state')) {
                    const noResults = document.createElement('div');
                    noResults.className = 'empty-state no-results-state glass-card';
                    noResults.innerHTML = `
                        <div class="empty-icon">
                            <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                                <circle cx="11" cy="11" r="8"></circle>
                                <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                            </svg>
                        </div>
                        <h2>No contacts found</h2>
                        <p>No results match "${e.target.value}". Try checking the spelling or searching for another contact name, email, or phone number.</p>
                    `;
                    document.querySelector('.contacts-grid').after(noResults);
                }
            } else {
                const noResults = document.querySelector('.no-results-state');
                if (noResults) {
                    noResults.remove();
                }
            }
        });
    }

    // 2. Add keyboard shortcuts
    document.addEventListener('keydown', (e) => {
        // Clear search on Escape
        if (e.key === 'Escape' && searchInput === document.activeElement) {
            searchInput.value = '';
            searchInput.dispatchEvent(new Event('input'));
            searchInput.blur();
        }
    });

    // 3. Staggered fade-in entrance for contact cards
    const cards = document.querySelectorAll('.contact-card');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(15px)';
        card.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
        
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 60);
    });
});
