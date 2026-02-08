# ADR 001: Use Playwright for Web Scraping

**Status**: Accepted  
**Date**: 2025-02-07  
**Deciders**: Development Team

## Context

The AOW4 Tome Scraper needs to extract data from the AOW4 Wiki (https://aow4.paradoxwikis.com). The Wiki uses dynamic JavaScript rendering, which means the content is not immediately available in the raw HTML.

## Decision

We will use **Playwright** for web scraping instead of traditional HTTP request libraries.

## Consequences

### Positive

- **JavaScript Support**: Playwright can execute JavaScript and wait for dynamically loaded content
- **Modern API**: Better async/await support compared to Selenium
- **Performance**: Faster than Selenium in most scenarios
- **Reliability**: Automatically handles waiting for elements to be ready
- **Cross-platform**: Works consistently on Linux, macOS, and Windows

### Negative

- **Dependency Size**: Requires installing browser binaries (~100MB)
- **Resource Usage**: Higher memory usage than simple HTTP requests
- **Complexity**: More complex setup than requests+BeautifulSoup

## Alternatives Considered

### requests + BeautifulSoup

**Rejected**: The AOW4 Wiki uses JavaScript to render content dynamically. Using requests would only get the initial HTML without the actual Tome data.

### Selenium

**Rejected**: While Selenium can handle JavaScript, Playwright offers:
- Better async/await support
- More modern and actively maintained
- Faster execution
- Better Python integration

### Scrapy

**Rejected**: Scrapy is a full web scraping framework that would be overkill for this simple use case. We only need to scrape two types of pages (list and detail).

## Implementation

```python
from playwright.async_api import async_playwright

async with async_playwright() as p:
    browser = await p.chromium.launch()
    page = await browser.new_page()
    await page.goto(url)
    content = await page.content()
```

## References

- [Playwright Documentation](https://playwright.dev/python/)
- [AOW4 Wiki](https://aow4.paradoxwikis.com/Tomes)
