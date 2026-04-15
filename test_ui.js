const { chromium } = require('playwright');
const path = require('path');

(async () => {
    const browser = await chromium.launch();
    const page = await browser.newPage();
    const filePath = 'file:///' + path.resolve('index.html').replace(/\\/g, '/');
    await page.goto(filePath);
    
    // Wait for the geojson to load and UI to populate
    await page.waitForTimeout(2000);
    
    // Click 'Vitórias' chip to make sure we're in that mode (optional, but good)
    const btnVitorias = await page.#chip-vencidos;
    if (btnVitorias) await btnVitorias.click();
    
    const options = await page.eval('#select-vencidos-candidate option', opts => opts.map(o => o.value + ': ' + o.textContent));
    console.log("Vencidos Options for 2002:", options);

    // Switch to 2000
    const btn2000 = await page.#chip-year-2000;
    if (btn2000) await btn2000.click();
    await page.waitForTimeout(2000);
    const options2000 = await page.eval('#select-vencidos-candidate option', opts => opts.map(o => o.value + ': ' + o.textContent));
    console.log("Vencidos Options for 2000:", options2000);

    // Switch to Guarulhos
    await page.selectOption('#select-municipio', 'GUARULHOS');
    await page.waitForTimeout(1000);
    const optionsGru = await page.eval('#select-vencidos-candidate option', opts => opts.map(o => o.value + ': ' + o.textContent));
    console.log("Vencidos Options for 2000 Guarulhos:", optionsGru);

    await browser.close();
})();
