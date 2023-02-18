import fetch from 'node-fetch';
import cheerio from 'cheerio';

async function downloadAndExtractLinks(url: string) {
  // Faz a requisição HTTP para obter o HTML da página
  const response = await fetch(url);
  const html = await response.text();

  // Usa o Cheerio para analisar o HTML e extrair os links
  const $ = cheerio.load(html);
  const links = $('a').map((_, el) => $(el).attr('href')).get();

  // Exibe os links na saída do console
  console.log(links);
}

downloadAndExtractLinks('https://www.example.com');
