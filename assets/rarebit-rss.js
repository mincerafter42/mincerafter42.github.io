// usage: run the command `node rarebit-rss.js`. make sure you have <https://nodejs.org/> installed.
// STUFF WHICH YOU SHOULD SET TO YOUR OWN COMIC'S INFO
const url = 'https://rarebit.neocities.org/rarebit/'; // base URL (make sure to include the slash at the end)
const title = 'Rarebit Example'; // title of the RSS feed
const outputFile = 'feed.rss'; // name of file to output to
// END OF STUFF

const https = require('node:https');
const fs = require('node:fs');

const location = {search:''}; // dummy object so rarebit doesn't throw errors

const entityEscape = str => str.replaceAll('&','&amp;').replaceAll('"','&quot;').replaceAll("'",'&apos;').replaceAll('<','&lt;').replaceAll('>','&gt;');

https.get(url+'js/comic_settings.js',res=>{
	let concat='';
	res.on('data',data=>concat+=data);
	res.on('end',()=>{ // here we have incredibly kludgy code
		concat+=`
			function writeDate(year, month, ...dayEtc) {return new Date(year, month-1, ...dayEtc).toUTCString()} // overwrite writeDate to RSS feed format
			const realMaxPg = Math.max(maxpg,pgData.reduce((accum,current)=>Math.max(current.pgNum,accum),0)); // because SOMEONE didn't update their maxpg correctly
			let rss='<?xml version="1.0" encoding="utf-8"?><rss version="2.0"><channel>';
			rss += '<title>'+entityEscape(title)+'</title>';
			rss += '<link>'+entityEscape(url)+'</link>';
			for (let i=realMaxPg;i>Math.max(realMaxPg-10,0);--i) {
				const page = pgData.find(x=>x.pgNum==i)||{};
				rss += '<item>';
				rss += '<title>'+entityEscape(page.title||'Page '+i)+'</title>';
				rss += '<guid isPermaLink="true">'+entityEscape(url+'?pg='+i)+'</guid>';
				if (page.date) rss += '<pubDate>'+entityEscape(page.date)+'</pubDate>';
				rss += '<description>'+entityEscape('<div>');
				if (page.imageFiles>1) {
					for (let j=1;j<=page.imageFiles;++j) {
						rss += entityEscape('<img src="'+entityEscape(url+folder+'/'+image+i+imgPart+j+'.'+ext)+(j==1&&page.altText?'" title="'+entityEscape(page.altText)+'">':'">'));
						if (j<page.imageFiles) rss += entityEscape('<br>');
					}
				} else rss += entityEscape('<img src="'+entityEscape(url+folder+'/'+image+i+'.'+ext)+(page.altText?'" title="'+entityEscape(page.altText)+'">':'">'));
				rss += entityEscape('</div>');
				rss += entityEscape(page.authorNotes||'')
				rss += '</description>';
				rss += '</item>';
			}
			rss+='</channel></rss>';
			fs.writeFileSync(outputFile,rss);
		`;
		eval(concat); // yes yes `eval` is a security risk. only run this on your own rarebit code ok
	});
});
// SPDX-License-Identifier: Unlicense
