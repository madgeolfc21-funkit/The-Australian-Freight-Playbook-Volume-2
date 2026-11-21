const { chromium } = require('playwright');
const path = require('path');
const OUT = path.join(__dirname, '..', 'The_Australian_Freight_Playbook_Volume_2_Review_Draft.pdf');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 794, height: 1123 } });
  p.on('console', m => console.log('console:', m.text()));
  p.on('pageerror', e => console.log('ERR', e.message));
  await p.goto('file://' + path.join(__dirname, 'book.html'));
  await p.waitForFunction(() => window.__done === true, null, { timeout: 180000 });
  const r = await p.evaluate(() => window.__report);
  console.log(JSON.stringify(r));
  // check for overflow per page and headings at bottom
  const issues = await p.evaluate(() => {
    const out = [];
    document.querySelectorAll('.page').forEach((pg, k) => {
      const b = pg.querySelector('.body'); if (!b) return;
      if (b.scrollHeight > b.clientHeight + 1) out.push(['overflow', k + 1]);
      const last = Array.from(b.children).filter(c => !c.classList.contains('notes')).pop();
      if (last && (/^H[23]$/.test(last.tagName) || last.classList.contains('leadin'))) out.push(['orphan', k + 1, last.textContent.slice(0, 50)]);
    });
    return out;
  });
  console.log('ISSUES', JSON.stringify(issues));
  await p.pdf({ path: OUT, preferCSSPageSize: true, printBackground: true });
  await b.close();
})();
