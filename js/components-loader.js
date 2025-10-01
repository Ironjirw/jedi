/**
 * Components Loader
 * Loads reusable header and footer components into all pages
 */

// Load header component
async function loadHeader() {
    try {
        const response = await fetch('/components/header.html');
        const html = await response.text();
        const headerPlaceholder = document.getElementById('header-placeholder');
        if (headerPlaceholder) {
            headerPlaceholder.innerHTML = html;
        }
    } catch (error) {
        console.error('Error loading header:', error);
    }
}

// Load footer component
async function loadFooter() {
    try {
        const response = await fetch('/components/footer.html');
        const html = await response.text();
        const footerPlaceholder = document.getElementById('footer-placeholder');
        if (footerPlaceholder) {
            footerPlaceholder.innerHTML = html;
        }
    } catch (error) {
        console.error('Error loading footer:', error);
    }
}

// Header scroll effect with section-based background (from index.html)
function updateHeaderBackground() {
    const header = document.getElementById('header');
    if (!header) return;

    const sections = document.querySelectorAll('section');
    const footer = document.querySelector('footer');
    const headerHeight = header.offsetHeight;
    const heroSection = document.querySelector('.hero');

    if (window.scrollY > 50) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }

    // Detect which section the navbar is over
    let currentSection = null;

    // Check footer first
    if (footer) {
        const footerRect = footer.getBoundingClientRect();
        if (footerRect.top <= headerHeight && footerRect.bottom >= 0) {
            currentSection = { className: 'footer' };
        }
    }

    // If not over footer, check sections
    if (!currentSection) {
        sections.forEach(section => {
            const rect = section.getBoundingClientRect();
            // Check if the navbar is over this section
            if (rect.top <= headerHeight && rect.bottom >= 0) {
                currentSection = section;
            }
        });
    }

    // Override: if at the very top with no scrolling, keep hero transparent
    if (heroSection && window.scrollY === 0) {
        currentSection = heroSection;
    }

    // Remove all section classes
    header.classList.remove('over-hero', 'over-stats', 'over-value-props', 'over-services', 'over-client-trust', 'over-quick-actions', 'over-cta', 'over-footer');

    // Add the appropriate section class
    if (currentSection) {
        const sectionClass = currentSection.className.split(' ')[0];
        header.classList.add('over-' + sectionClass);
    }
}

// Load all components when DOM is ready
document.addEventListener('DOMContentLoaded', async function() {
    await Promise.all([loadHeader(), loadFooter()]);

    // Initialize header scroll effects after components are loaded
    window.addEventListener('scroll', updateHeaderBackground);
    // Run once on load to set initial state
    window.addEventListener('load', updateHeaderBackground);
    // Run immediately after loading components
    updateHeaderBackground();
});