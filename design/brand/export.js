const {chromium}=require('/tmp/claude-0/-home-user-Jaywesterlow/86f051b3-dc94-54d0-8f4b-a6ade69d3854/scratchpad/node_modules/playwright');
const fs=require('fs');const path=require('path');
const L='/home/user/Jaywesterlow/design/brand/logos', O='/home/user/Jaywesterlow/design/brand/export';
fs.mkdirSync(O,{recursive:true});
const jobs=[ ['b-dak-og.svg','og-1200x630.png',1200,false],
];
(async()=>{const b=await chromium.launch();
for(const [svg,out,w,tr] of jobs){const s=fs.readFileSync(path.join(L,svg),'utf8');const m=s.match(/viewBox="0 0 ([\d.]+) ([\d.]+)"/);const h=Math.round(w*m[2]/m[1]);
 const p=await b.newPage({viewport:{width:w,height:h}});
 await p.setContent(`<html><body style="margin:0;background:${tr?'transparent':'#fff'}">${s.replace(/width="[\d.]+" height="[\d.]+"/,`width="${w}" height="${h}"`)}</body></html>`);
 await p.screenshot({path:path.join(O,out),omitBackground:tr});await p.close();console.log(out,w+'x'+h);}
await b.close();})();
