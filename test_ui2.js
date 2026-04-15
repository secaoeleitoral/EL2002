
const { chromium } = require('playwright');
const path = require('path');

(async () => {
    try {
        const browser = await chromium.launch();
        const page = await browser.newPage();
        const filePath = 'file:///' + path.resolve('index.html').replace(/\\/g, '/');
        await page.goto(filePath);
        
        await page.waitForTimeout(2000); // let geojson load
        
        const options = await page.\$\('#select-vencidos-candidate option', opts => opts.map(o => o.value + ': ' + o.textContent));
        console.log('2002 Global Options:', options);

        await page.click('#chip-year-2000');
        await page.waitForTimeout(2000);
        const optionsGru = await page.\$\('#select-vencidos-candidate option', opts => opts.map(o => o.value + ': ' + o.textContent));
        console.log('2000 Global Options:', optionsGru);

        await browser.close();
    } catch(err) {
        console.error(err);
    }
})();
