---
layout: default
title: "FIAT/IFTA 2026: página da palestra"
nav_exclude: true
permalink: /fiat-ifta-2026-companion/pt-br/
fc_lang: pt-br
description: Exemplos em tamanho real e notas da palestra de Fabio Bedoya na FIAT/IFTA 2026, Os limites atuais da IA na restauração de filmes e como podem ser superados.
---

{% include fiat-companion/style.html %}

<div class="fc" lang="pt-BR">

{% include fiat-companion/langswitch.html %}

<header class="fc-hero">
  <p class="fc-kicker">Conferência Mundial FIAT/IFTA · São Paulo 2026</p>
  <h1 id="the-current-limits-of-ai-in-film-restoration">Os limites atuais da IA na restauração de filmes e como podem ser superados</h1>
  <p class="fc-byline">Fabio Bedoya<span>Diretor de Restauração, Filmfinity</span></p>
  <p class="fc-panel">Cinemateca Brasileira<span>8 de outubro de 2026</span></p>
  <div class="fc-buttons">
    <a class="fc-btn fc-btn-primary" href="https://github.com/fabiocolor/custom-machine-learning-for-film-restoration">A pesquisa no GitHub</a>
    <a class="fc-btn" href="#workflows">Fluxos de trabalho e guias</a>
  </div>
  <p>Esta página acompanha a minha palestra. Ela segue os slides na ordem, então você pode encontrar a versão em tamanho real de cada exemplo à medida que ele aparece, ou voltar a ela depois. Para cada experimento, anotei o que funcionou e onde ainda há limitações.</p>
</header>

<p class="fc-tip">Toque em um vídeo para assistir aqui mesmo. O player transmite do Google Drive, então pode mostrar uma qualidade menor que a do original, principalmente em uma conexão lenta. Para ver os detalhes, use “Original em tamanho real” abaixo de cada vídeo: ele baixa o arquivo original, que você pode abrir no player de vídeo do celular ou do computador. Abaixo de cada imagem, os botões abrem cada imagem em tamanho real. É melhor baixar os arquivos grandes pelo Wi-Fi. A maioria dos vídeos são comparações lado a lado, então cada metade é menor que o arquivo completo.</p>

<nav class="fc-toc" aria-labelledby="contents">
  <h2 id="contents">Acompanhe a palestra</h2>
  <ol>
    <li><a href="#copycat-to-open-weight"><span class="fc-n">2</span>Do CopyCat aos modelos de pesos abertos</a></li>
    <li><a href="#masking-versus-recovery"><span class="fc-n">3</span>Mascarar versus recuperar</a></li>
    <li><a href="#the-limits"><span class="fc-n">4</span>As limitações<span class="fc-v">Imagens</span></a></li>
    <li><a href="#reference-recovery"><span class="fc-n">5–6</span>Recuperação de cor com referência<span class="fc-v">Vídeo</span></a></li>
    <li><a href="#synthetic-reference"><span class="fc-n">7</span>Criando uma referência sintética<span class="fc-v">Imagens</span></a></li>
    <li><a href="#telestyle"><span class="fc-n">8–9</span>Mantendo a cor estável ao longo de um plano<span class="fc-v">Vídeo</span></a></li>
    <li><a href="#h3-controlnet"><span class="fc-n">10–11</span>Tornando o processo mais rápido<span class="fc-v">Vídeo</span></a></li>
    <li><a href="#temporal-cbcr"><span class="fc-n">12–13</span>O adaptador Temporal CbCr<span class="fc-v">Vídeo</span></a></li>
    <li><a href="#diffusion-upscaling"><span class="fc-n">14–15</span>Upscaling por difusão<span class="fc-v">Vídeo</span></a></li>
    <li><a href="#diffusion-reconstruction"><span class="fc-n">16–17</span>Reconstrução por difusão</a></li>
    <li><a href="#combining-sources"><span class="fc-n">18–19</span>Combinando fontes e depois reconstruindo<span class="fc-v">Vídeo</span></a></li>
    <li><a href="#dialogue-recovery"><span class="fc-n">20</span>Recuperação de diálogos</a></li>
    <li><a href="#inside-existing-tools"><span class="fc-n">21</span>IA dentro das ferramentas que já usamos<span class="fc-v">Vídeo</span></a></li>
    <li><a href="#limits-now"><span class="fc-n">22</span>Onde estão as limitações hoje</a></li>
    <li><a href="#thanks"><span class="fc-n">23</span>Agradecimentos e créditos</a></li>
  </ol>
</nav>

<section class="fc-section" id="copycat-to-open-weight">
  <p class="fc-slide">Slide 2</p>
  <h2 id="copycat-to-open-weight-title">Do CopyCat aos modelos de pesos abertos</h2>
  <p>Minha pesquisa começou com o CopyCat, dentro do Nuke. A ideia é treinar um modelo pequeno para cada filme a partir de quadros correspondentes de duas cópias: a digitalização danificada e uma cópia melhor do mesmo filme, que mostra o resultado que queremos. Foi isso que apresentei no ano passado em Roma, e continua sendo a minha base de comparação. Mas o método precisa dessa cópia melhor para aprender, e é uma plataforma fechada, feita para efeitos visuais.</p>
  <p>Desde então, os modelos de pesos abertos, aqueles que qualquer pessoa pode baixar e rodar, ficaram bons o bastante para imagem, vídeo e voz em uma única estação de trabalho. As pessoas já usam esses modelos para “restaurar” fotos antigas e filmes caseiros, mas quase sempre fora do arquivo. Então a minha pergunta é: como podemos restringi-los para que se tornem úteis para o trabalho que realmente precisamos fazer?</p>
</section>

<section class="fc-section" id="masking-versus-recovery">
  <p class="fc-slide">Slide 3</p>
  <h2 id="masking-versus-recovery-title">Mascarar versus recuperar</h2>
  <p>A maioria das ferramentas de restauração usa filtros espaciais e temporais. Elas pegam imagem emprestada do mesmo quadro, ou dos quadros ao redor, e quando não há nada limpo para copiar, elas interpolam. O slide mostra o Dry Clean no Phoenix em <em>Point Blank</em> (1967); as marcas vermelhas são o que ele detectou e removeu.</p>
  <p>Essas ferramentas conseguem esconder poeira, riscos e cintilação, e preencher dois ou três quadros faltantes. Mas não conseguem trazer de volta o que se perdeu. Sendo honestos, a restauração digital sempre foi sobre mascarar, não sobre recuperar.</p>
  <p>Por isso, a IA na restauração não é algo completamente novo. O que ela nos dá é uma forma de enfrentar problemas que antes não eram viáveis, técnica ou financeiramente, trabalhando com a digitalização do jeito que ela está. Em muitos arquivos, principalmente na América Latina e no Sudeste Asiático, essa digitalização desbotada é tudo o que resta de um filme.</p>
</section>

<section class="fc-section" id="the-limits">
  <p class="fc-slide">Slide 4</p>
  <h2 id="the-limits-title">As limitações</h2>
  <p>Do meu ponto de vista, há três limitações principais.</p>
  <ul class="fc-points">
    <li><strong>Eles não foram feitos para filme.</strong> Esses modelos foram criados para gerar ou editar imagens nascidas digitais. Eles suavizam o grão e os detalhes finos, ou inventam detalhes novos. A imagem parece mais nítida, mas deixa de parecer filme.</li>
    <li><strong>Resolução e duração.</strong> Nos meus testes, os modelos de vídeo locais trabalharam em torno de 768 × 432 pixels e só conseguiam acompanhar cerca de dez segundos de cada vez. No slide, o Qwen Image Edit rodou duas vezes em um quadro de <em>Reptilicus</em> (1961) com o mesmo prompt: uma vez no quadro inteiro (1184 × 880) e outra em quatro blocos unidos (2048 × 1556). Observe a torre do salva-vidas: os blocos preservam mais do grão e dos detalhes do filme, mas a cor varia entre eles e as emendas aparecem. Dividir em blocos ajuda, mas traz um novo problema para resolver.</li>
    <li><strong>Custo.</strong> A restauração exige muitas iterações, e na nuvem cada uma delas custa dinheiro. Por isso eu trabalho localmente, mas isso ainda significa hardware, tempo e eletricidade. Não existe processamento de graça, mesmo que o computador seja seu.</li>
  </ul>

  <figure class="fc-media fc-still">
    <a href="{{ '/images_kebab/seapavaa2026/reptilicus_beach_tiled_vs_fullframe_raw_inference.png' | relative_url }}"><img src="{{ '/images_kebab/seapavaa2026/reptilicus_beach_tiled_vs_fullframe_raw_inference.png' | relative_url }}" alt="Quadro de Reptilicus na praia: quatro blocos unidos à esquerda e o quadro inteiro em uma única passada à direita" width="1732" height="770" loading="lazy" decoding="async"></a>
    <p class="fc-bar">Slide 4 · <em>Reptilicus</em> (1961): quatro blocos unidos (à esquerda) e o quadro inteiro em uma única passada (à direita)</p>
    <figcaption class="fc-body">
      <p class="fc-file">Imagens em tamanho real</p>
      <ul class="fc-links">
        <li><a class="fc-full" href="{{ '/images_kebab/seapavaa2026/originals/reptilicus_t001_tiling/reptilicus_t001_fullframe_clara_baseline_frame_000000_test.png' | relative_url }}">Quadro inteiro · 1184 × 880</a></li>
        <li><a class="fc-full" href="{{ '/images_kebab/seapavaa2026/originals/reptilicus_t001_tiling/reptilicus_t001_four_tile_raw_inference_hard_stitch.png' | relative_url }}">Quatro blocos · 2048 × 1556</a></li>
      </ul>
    </figcaption>
  </figure>
</section>

<section class="fc-section" id="reference-recovery">
  <p class="fc-slide">Slides 5–6</p>
  <h2 id="reference-recovery-title">Recuperação de cor com referência</h2>
  <p>Vamos começar pelo que já funciona. Um modelo pequeno é treinado com pares de quadros correspondentes: a fonte desbotada e uma referência que ainda tem a cor. Essa referência pode ser uma telecinagem, um DVD, outra cópia ou o negativo original, onde os dois coincidirem.</p>
  <p>O modelo aprende apenas a cor. O resultado dele é combinado com a luma, ou seja, o brilho, da digitalização original, então a resolução, o grão e os detalhes continuam como estavam. O fluxo de trabalho está <a href="{{ '/chroma-recovery/' | relative_url }}">documentado aqui</a>.</p>
  <div class="fc-missing"><p>O trecho mostrado no slide 6 não está incluído nesta página. Abaixo há outro exemplo do mesmo método.</p></div>

  <figure class="fc-media">
{% include fiat-companion/video.html key="candy" title="Candy Candy: digitalização original, digitalização equilibrada, referência em DVD e recuperação de cor" label="Assistir ao vídeo: Candy Candy, recuperação de cor com referência (1 minuto e 10 segundos)" %}
    <figcaption class="fc-body">
      <h3 id="candy-candy-title">Candy Candy: a cor a partir de uma referência em DVD</h3>
      <p>A cor de um DVD francês PAL correspondente é transferida para uma digitalização desbotada em 16mm. Quatro versões aparecem lado a lado: a digitalização original, a digitalização depois de equilibrada e limpa, a referência em DVD e o resultado do modelo.</p>
      <div class="fc-verdict">
        <div><strong>O que funcionou</strong><p>O resultado tira a cor do DVD, enquanto os detalhes vêm da digitalização em 16mm.</p></div>
        <div><strong>Limitações</strong><p>O método só é tão bom quanto a sua referência. Este DVD é em definição padrão e tem as suas próprias escolhas de correção de cor e de transferência. E muitos filmes já não têm nenhuma referência.</p></div>
      </div>
{% include fiat-companion/files.html key="candy" desc="comparação 1920 × 1080 · 1 min 10 s · 24 fps" %}
      <details>
        <summary>Resultado em resolução total (4400 × 3300, cerca de 298 MB)</summary>
        <p>A digitalização com a cor recuperada, sozinha, no tamanho total da digitalização, 4400 × 3300. Sem som, 24 fps, HEVC. É um arquivo grande, então é melhor baixá-lo pelo Wi-Fi. O player do Drive pode transmitir uma versão menor; baixe o arquivo para ver a resolução total.</p>
{% include fiat-companion/files.html key="candy-full" %}
      </details>
    </figcaption>
  </figure>
</section>

<section class="fc-section" id="synthetic-reference">
  <p class="fc-slide">Slide 7</p>
  <h2 id="synthetic-reference-title">Criando uma referência sintética</h2>
  <p>E o que acontece quando não existe referência? Você cria uma: um quadro de cor aprovado para cada plano. Eu chamo isso de referência sintética, e faço com o Qwen Image Edit, um modelo de imagem de pesos abertos da Alibaba.</p>
  <p>A minha primeira tentativa foi guiá-lo com uma leader lady, a mulher dos quadros de calibração no início de um rolo. Não funcionou. Esses modelos não entendem significado como nós, então, em vez de pegar só a cor, o modelo misturou as duas imagens e a mulher acabou entrando no plano. Eu chamo isso de contaminação semântica.</p>
  <p>Uma carta de cores simples funcionou melhor, depois que eu a desfoquei levemente. Ela guia a cor sem dar ao modelo mais nada para copiar.</p>

  <p>Depois veio o prompt, que é a forma de conversar com o modelo. Fiz um pequeno concurso, que chamei de America's Next Top Machine Learning Model: dezenas de prompts e centenas de quadros de teste, em sete rodadas com sete filmes desbotados. Um prompt só passava de uma rodada se oito de cada dez quadros fossem aceitáveis. A fileira de baixo do slide mostra um quadro desbotado de <em>Counter Attack</em>, um filme chinês de 1976, com três dos finalistas. O vencedor, Clara, é o que eu mais uso, mas também uso os outros, dependendo do plano.</p>
  <p>Da referência sintética eu fico só com a cor. O brilho continua vindo da digitalização.</p>

  <figure class="fc-media fc-still">
    <a href="{{ '/images_kebab/seapavaa2026/leader_lady_semantic_contamination_gar01_triptych.png' | relative_url }}"><img src="{{ '/images_kebab/seapavaa2026/leader_lady_semantic_contamination_gar01_triptych.png' | relative_url }}" alt="Três quadros: a fonte desbotada, o resultado guiado por uma leader lady com a mulher misturada ao plano e o resultado guiado por uma carta de cores" width="1388" height="416" loading="lazy" decoding="async"></a>
    <p class="fc-bar">Slide 7 · A fonte desbotada, o resultado guiado por uma leader lady e o resultado guiado por uma carta de cores</p>
    <figcaption class="fc-body">
      <p class="fc-file">Imagens em tamanho real</p>
      <ul class="fc-links">
        <li><a class="fc-full" href="{{ '/images_kebab/seapavaa2026/originals/leader_lady_gar01/01_raw_source.png' | relative_url }}">Fonte desbotada · 2048 × 1556</a></li>
        <li><a class="fc-full" href="{{ '/images_kebab/seapavaa2026/originals/leader_lady_gar01/02_early_marcie_contamination.png' | relative_url }}">Leader lady · 1168 × 888</a></li>
        <li><a class="fc-full" href="{{ '/images_kebab/seapavaa2026/originals/leader_lady_gar01/03_belak_chart_corrected.png' | relative_url }}">Carta de cores · 1184 × 880</a></li>
      </ul>
      <div class="fc-missing" style="margin-top: 0.8rem"><p>Os prompts finalistas da fileira de baixo do slide não estão incluídos nesta página.</p></div>
    </figcaption>
  </figure>
</section>

<section class="fc-section" id="telestyle">
  <p class="fc-slide">Slides 8–9</p>
  <h2 id="telestyle-section-title">Mantendo a cor estável ao longo de um plano</h2>
  <p>Conseguir um quadro convincente já não é a parte difícil. Se você simplesmente rodar o modelo 24 vezes por segundo, não funciona, porque esses modelos não são determinísticos: cada execução é um pouco uma roleta. Cada quadro recebe uma interpretação ligeiramente diferente, e a cor cintila.</p>
  <p>O slide 8 mostra uma cena de dança de <em>Obsession</em> em que cada quadro foi recuperado separadamente. Observe o vestido da mulher à direita e o fundo. Cada quadro, sozinho, é uma interpretação razoável, mas juntos eles não combinam. Um bom quadro é uma miniatura. Uma restauração precisa que o plano inteiro seja coerente consigo mesmo. Isso é consistência temporal, e foi o maior obstáculo.</p>

  <figure class="fc-media">
{% include fiat-companion/video.html key="slide09" title="Counter Attack: uma referência para o plano inteiro (TeleStyle)" label="Assistir ao vídeo: Counter Attack, uma referência para o plano inteiro (11 segundos)" %}
    <p class="fc-bar">Slide 9 · <em>Counter Attack</em> (1976): uma referência para o plano inteiro (TeleStyle)</p>
    <figcaption class="fc-body">
      <p>O TeleStyle, da TeleAI, é um LoRA: um pequeno complemento para o Qwen Image Edit, feito para copiar o estilo de uma imagem para outra. Eu pego uma referência aprovada e copio a cor dela para cada quadro do plano.</p>
      <div class="fc-verdict">
        <div><strong>O que funcionou</strong><p>A cor se mantém ao longo do plano inteiro.</p></div>
        <div><strong>Limitações</strong><p>Ele roda o modelo em cada quadro, um por um, e cada quadro ainda precisou ser conferido, seed após seed. Este plano de 11 segundos levou quase quatro horas. Serve como teste, mas não é algo que dê para usar em um longa-metragem.</p></div>
      </div>
{% include fiat-companion/files.html key="slide09" desc="comparação 1920 × 1080 · 11 s · 30 fps" %}
    </figcaption>
  </figure>
</section>

<section class="fc-section" id="h3-controlnet">
  <p class="fc-slide">Slides 10–11</p>
  <h2 id="h3-controlnet-section-title">Tornando o processo mais rápido: H3 e ControlNet</h2>
  <p>Eu tinha uma cor que se mantinha, mas o processo demorava demais. No fim de julho, a MiniMax lançou o H3, um modelo de vídeo muito bom com imagens de referência. Em uma única passada, ele leva a cor aprovada por um trecho inteiro de um plano.</p>
  <p>Sozinho, porém, o H3 se afasta da imagem e perde a geometria. Então eu tive que rodá-lo em trechos curtos e fazer com que todos combinassem, o que significava mais processamento e mais tempo. Depois, em agosto, a Alibaba PAI lançou um ControlNet para o H3. Um ControlNet é uma forma de direcionar o que o modelo faz; este fornece ao modelo as bordas de cada quadro, o que ajuda a manter a geometria e o movimento do próprio filme.</p>
  <p>Eu fico só com a cor e a coloco sobre o brilho original, para que o grão, a aspereza e até a sujeira permaneçam. Deixados por conta própria, esses modelos querem mudar tudo e deixar a imagem com aspecto de plástico.</p>

  <figure class="fc-media">
{% include fiat-companion/video.html key="slide11" title="Counter Attack: H3 e ControlNet, finalizado com o adaptador Temporal CbCr" label="Assistir ao vídeo: Counter Attack, H3 e ControlNet (13 segundos)" %}
    <p class="fc-bar">Slide 11 · <em>Counter Attack</em>: H3 + ControlNet, finalizado com o adaptador Temporal CbCr</p>
    <figcaption class="fc-body">
      <p>A cor vem do H3 com o ControlNet, e é finalizada com o adaptador Temporal CbCr, explicado na próxima seção. Escolhi este plano porque ele é difícil: muito movimento, uma multidão que muda o tempo todo e uma panorâmica rápida no meio.</p>
      <div class="fc-verdict">
        <div><strong>O que funcionou</strong><p>A cor se mantém durante todo esse movimento, e a geometria continua igual à do original.</p></div>
        <div><strong>Limitações</strong><p>Olhando de perto, há um pouco de dominante de cor nas sombras. A minha cópia estava a 30 quadros por segundo com a cadência quebrada, então foi difícil extrair quadros limpos dela, e o adaptador precisa de quadros bem alinhados. Ainda estou trabalhando nisso.</p></div>
      </div>
{% include fiat-companion/files.html key="slide11" desc="comparação 1920 × 840 · 13 s · 24 fps" %}
    </figcaption>
  </figure>
</section>

<section class="fc-section" id="temporal-cbcr">
  <p class="fc-slide">Slides 12–13</p>
  <h2 id="temporal-cbcr-section-title">O adaptador Temporal CbCr</h2>
  <p>Esta é a ideia por trás do meu trabalho com o CopyCat, levada para fora do Nuke para que a pesquisa possa rodar em uma plataforma aberta. CbCr são os dois canais de cor de uma imagem de vídeo, mantidos separados do brilho.</p>
  <p>Eu rodo o H3 ou o TeleStyle uma ou duas vezes, dependendo da duração do plano, e fico só com os quadros que passam na revisão. Eu os chamo de professores. Eles não precisam cobrir o plano inteiro, desde que a geometria deles esteja alinhada com a imagem.</p>
  <p>Um modelo pequeno, com menos de um milhão de parâmetros, aprende a cor do plano a partir dos professores em poucos minutos. Depois, ele preenche os quadros que não têm professor e mantém a cor estável ao longo de todo o plano. No slide 12, o primeiro e o terceiro quadros não têm professor, e o segundo e o quarto têm.</p>

  <figure class="fc-media">
{% include fiat-companion/video.html key="slide13" title="Unman, Wittering and Zigo: adaptador Temporal CbCr" label="Assistir ao vídeo: Unman, Wittering and Zigo, adaptador Temporal CbCr (7 segundos)" %}
    <p class="fc-bar">Slide 13 · <em>Unman, Wittering and Zigo</em> (1971): adaptador Temporal CbCr</p>
    <figcaption class="fc-body">
      <p>Uma cena de coral, com a fonte desbotada à esquerda e o resultado do adaptador à direita. Os professores cobriram 101 dos 164 quadros, e o adaptador preencheu o restante. O treinamento levou cerca de um minuto e meio.</p>
      <div class="fc-verdict">
        <div><strong>O que funcionou</strong><p>Ele preserva tudo o que está no original: a sujeira, a aspereza do filme. Até o vitral atrás do coral se mantém consistente durante toda a panorâmica.</p></div>
        <div><strong>Limitações</strong><p>O adaptador só é tão bom quanto os seus professores, e precisa de quadros bem alinhados. A cor continua sendo uma interpretação, a menos que uma referência sobrevivente a confirme.</p></div>
      </div>
{% include fiat-companion/files.html key="slide13" desc="comparação 1920 × 850 · 7 s · 24 fps" %}
    </figcaption>
  </figure>
</section>

<section class="fc-section" id="diffusion-upscaling">
  <p class="fc-slide">Slides 14–15</p>
  <h2 id="diffusion-upscaling-section-title">Upscaling por difusão</h2>
  <p>Até aqui, o modelo só acrescenta cor, e a digitalização mantém a sua própria imagem. Mas às vezes o elemento que sobreviveu não tem informação suficiente para uma restauração tradicional. Nossas ferramentas pegam emprestado do mesmo quadro ou dos quadros ao redor, e quando todos os quadros estão danificados, não sobra nada para pegar emprestado. O upscaling por difusão permite que um modelo de vídeo reconstrua a imagem a partir do que sobreviveu, seguindo a sua estrutura e o seu movimento.</p>
  <p><em>El Tinterillo</em> sobrevive apenas como uma cópia em 16mm danificada e uma telecinagem mais limpa, mas suave, cortada nas bordas e com a cadência estranha das telecinagens daquela época. Combinei as duas, com a telecinagem por dentro e o 16mm em volta, e depois limpei esse híbrido com um filtro de mediana. Isso dá um contorno aproximado para guiar a geometria, mas também remove os detalhes finos. Então, para definir como a imagem deveria ficar, fiz outra referência sintética com o ChatGPT Images. O MiniMax H3, no modo de referência, usa então essa imagem e o contorno para gerar cada trecho do plano.</p>

  <figure class="fc-media">
{% include fiat-companion/video.html key="slide15" title="El Tinterillo: upscaling por difusão, a escada" label="Assistir ao vídeo: El Tinterillo, upscaling por difusão (26 segundos)" %}
    <p class="fc-bar">Slide 15 · <em>El Tinterillo</em>: upscaling por difusão, a escada</p>
    <figcaption class="fc-body">
      <p>A digitalização original em 16mm está à esquerda, e o resultado que aprovei está à direita. Foi preciso um longo processo de iteração para chegar aqui.</p>
      <div class="fc-verdict">
        <div><strong>O que funcionou</strong><p>A imagem nesta digitalização não tem salvação com as ferramentas tradicionais. O H3 preenche essas lacunas e reconstrói a imagem, seguindo a estrutura e o movimento do original.</p></div>
        <div><strong>Limitações</strong><p>O resultado é parcialmente sintético: o modelo inventa detalhes finos que o filme já não tem, e isso precisa ser declarado. O modelo trabalhou em 768 × 432. Ainda há um salto de brilho no primeiro quadro, e os rostos e os detalhes finos continuam fracos.</p></div>
      </div>
      <p>Algumas pessoas vão chamar isso de heresia, e até certo ponto é. Eu mesmo não chamaria isso de restauração de filme propriamente dita. Mas, com um material como este, não vejo outro caminho, e talvez precisemos abrir a cabeça para o que a restauração pode ser.</p>
{% include fiat-companion/files.html key="slide15" desc="comparação 1920 × 756 · 26 s · 24 fps" %}
    </figcaption>
  </figure>
</section>

<section class="fc-section" id="diffusion-reconstruction">
  <p class="fc-slide">Slides 16–17</p>
  <h2 id="diffusion-reconstruction-title">Reconstrução por difusão</h2>
  <p>Às vezes a imagem não está danificada, ela simplesmente não existe mais: são quadros que faltam no único elemento sobrevivente. Isso acontece muito com nitrato, quando um trecho em decomposição foi cortado para não danificar o resto do rolo.</p>
  <p>Ferramentas como Phoenix, DIAMANT ou DaVinci Resolve conseguem preencher dois ou três quadros faltantes com fluxo óptico. Em uma lacuna mais longa, o movimento começa a parecer errado, porque elas só conseguem interpolar o que sobreviveu.</p>
  <p>Na palestra, o exemplo é uma lacuna de 15 quadros em um negativo de câmera cujo som ainda sobrevive, então a lacuna precisa ser preenchida para manter imagem e som juntos. Rastreei os atores do último quadro antes da lacuna até o primeiro quadro depois dela, e levei esse movimento pelos quadros faltantes: são os esqueletos do slide 16. Depois, o modelo de vídeo VACE, da Alibaba, gerou a imagem, guiado por esse movimento, somente dentro da lacuna.</p>
  <div class="fc-limits"><p><strong>O que funcionou, e as limitações.</strong> Os quadros gerados se sustentam bem, e todos os quadros originais permanecem intactos. A limitação de resolução do slide 4 continua valendo, e o que é gerado precisa ser declarado.</p></div>
  <div class="fc-missing" style="margin-top: 1rem"><p>O trecho mostrado no slide 17 não está incluído nesta página. O <a href="#combining-sources">exemplo de <em>Knight of the Trail</em></a> mais abaixo usa a mesma ideia em danos de nitrato.</p></div>
</section>

<section class="fc-section" id="combining-sources">
  <p class="fc-slide">Slides 18–19</p>
  <h2 id="combining-sources-section-title">Combinando fontes e depois reconstruindo</h2>
  <p>Quando vários elementos sobrevivem, normalmente cada um está danificado em lugares diferentes. O George Eastman Museum me enviou <em>Knight of the Trail</em> (1915) como uma cópia em nitrato e uma cópia de segurança em diacetato. Juntas, elas cobrem a maior parte do filme, mas em alguns pontos o nitrato se decompôs e a cópia de segurança também não tem esses quadros.</p>
  <p>Primeiro, eu junto os dois elementos. Eles tinham cor, deformação e enquadramento diferentes, então cada quadro de um é alinhado ao outro pelas suas características e deformado até se encaixar. Depois, uma única correção de tom, ajustada nos quadros correspondentes mais limpos, dá aos dois a mesma aparência.</p>
  <p>Em seguida, cada quadro vem do elemento que sobreviveu sem danos: 155 quadros da cópia em nitrato e 53 da cópia de segurança. A linha do tempo do slide 18 é um mapa disso, com laranja para o nitrato, azul para a cópia de segurança e vermelho onde nenhum dos dois sobreviveu. Nesses 18 quadros, eu mascaro apenas as áreas danificadas e reconstruo só essas áreas. A imagem que sobreviveu continua original, porque não queremos substituir um quadro inteiro só porque uma parte dele está danificada.</p>

  <figure class="fc-media">
{% include fiat-companion/video.html key="slide19" title="Knight of the Trail: reconstrução por difusão de danos de nitrato" label="Assistir ao vídeo: Knight of the Trail, reconstrução de danos de nitrato (9 segundos)" %}
    <p class="fc-bar">Slide 19 · <em>Knight of the Trail</em> (1915): reconstrução por difusão de danos de nitrato. Cortesia do George Eastman Museum.</p>
    <figcaption class="fc-body">
      <p>O original em nitrato está à esquerda, e o resultado aprovado está à direita.</p>
      <div class="fc-verdict">
        <div><strong>O que funcionou</strong><p>O resultado se sustenta bem, e aqui a resolução não é um grande problema.</p></div>
        <div><strong>Limitações</strong><p>Este é um teste de trabalho em 640 × 512, mostrado dentro de uma comparação em HD. Não é uma restauração nativa em HD.</p></div>
      </div>
{% include fiat-companion/files.html key="slide19" desc="comparação 1920 × 832 · 9 s · 24 fps · sem som" %}
    </figcaption>
  </figure>
</section>

<section class="fc-section" id="dialogue-recovery">
  <p class="fc-slide">Slide 20</p>
  <h2 id="dialogue-recovery-title">Recuperação de diálogos</h2>
  <p>A mesma ideia vale para o som: uma palavra muito distorcida pode ser reconstruída a partir da própria voz do ator.</p>
  <p>Usei o Fish Audio S2 Pro, um modelo de fala de pesos abertos, rodando localmente. Ele recebe alguns segundos de diálogo limpo do mesmo ator, tirados do filme, cerca de dez segundos neste caso, e as palavras exatas. Ele gera muitas tomadas da fala inteira. O reconhecimento de fala e a comparação de voz ajudam a classificá-las, mas quem decide é a escuta. Depois, só a parte danificada volta para o lugar, cerca de um terço de segundo aqui. Todo o resto é a trilha sonora original.</p>
  <div class="fc-limits"><p><strong>Limitações.</strong> O resultado do modelo saiu tão limpo que não se misturava, então acrescentei um pouco do ruído de fundo do próprio filme. Um ouvido treinado ainda pode perceber isso na palavra reparada.</p></div>
  <div class="fc-missing" style="margin-top: 1rem"><p>O exemplo de áudio da palestra não está incluído nesta página.</p></div>
</section>

<section class="fc-section" id="inside-existing-tools">
  <p class="fc-slide">Slide 21</p>
  <h2 id="inside-existing-tools-section-title">IA dentro das ferramentas que já usamos</h2>
  <p>A IA também pode trabalhar por meio das ferramentas que já usamos. As empresas que as fabricam estão incorporando a IA, tanto para controle e gerenciamento quanto para processamento. O DaVinci Resolve 21.1 permite que assistentes de IA o operem diretamente, o Premiere Pro tem um AI Assistant que trabalha dentro do projeto, e a Avid já mostrou IA agêntica para o Media Composer. As ferramentas de restauração podem funcionar da mesma forma.</p>

  <figure class="fc-media">
{% include fiat-companion/video.html key="slide21" title="Point Blank: um modelo trabalhando dentro do Phoenix" label="Assistir ao vídeo: Point Blank, um modelo trabalhando dentro do Phoenix (30 segundos)" %}
    <p class="fc-bar">Slide 21 · <em>Point Blank</em> (1967): um modelo trabalhando dentro do Phoenix</p>
    <figcaption class="fc-body">
      <p>Um dos meus testes de pesquisa. Depois que o Dry Clean roda no Phoenix, um modelo pinta as máscaras de proteção diretamente no projeto. O vermelho mostra o que o Dry Clean alterou.</p>
      <div class="fc-limits"><p><strong>Limitações.</strong> Ainda está em um estágio inicial. Esta é uma gravação de tela do fluxo de trabalho, não uma restauração finalizada.</p></div>
{% include fiat-companion/files.html key="slide21" desc="gravação de tela 1920 × 1080 · 30 s · 24 fps · sem som" %}
    </figcaption>
  </figure>
</section>

<section class="fc-section" id="limits-now">
  <p class="fc-slide">Slide 22</p>
  <h2 id="limits-now-title">Onde estão as limitações hoje</h2>
  <ul class="fc-points">
    <li>O que funcionou melhor foi manter a imagem do próprio filme e deixar o modelo acrescentar apenas o que falta: a cor, uma lacuna, uma palavra.</li>
    <li>A cor se mantém ao longo de um plano quando referências aprovadas guiam o plano inteiro, seja por meio de um modelo de vídeo, seja por meio do adaptador pequeno.</li>
    <li>O controle é o que mais ajuda. Bordas, movimento rastreado e registro mantêm o modelo preso ao filme, e não à ideia que ele faz do filme.</li>
    <li>No fluxo de trabalho de cor, um modelo pequeno aprende com quadros professores aprovados e preenche o plano, para que o modelo grande não precise rodar em todos os quadros.</li>
    <li>O que ainda precisa melhorar é a resolução e a duração. Os modelos ainda enxergam uma imagem reduzida, cerca de dez segundos de cada vez.</li>
    <li>Nada disso se resolve com um clique. Exige paciência, e um restaurador para decidir o que é aceitável e para dizer o que foi gerado.</li>
  </ul>
  <p>Há um ano, e até alguns meses atrás, nada disso era possível.</p>
</section>

<section class="fc-section" id="workflows">
  <h2 id="workflows-title">Fluxos de trabalho e guias</h2>
  <ul class="fc-points">
    <li><a href="{{ '/chroma-recovery/' | relative_url }}">Recuperação de cor treinada com referência</a>: aprender com quadros correspondentes da fonte e da referência e, depois, combinar a cor prevista com o brilho da digitalização.</li>
    <li><a href="{{ '/open-weight-color-recovery/' | relative_url }}">Recuperação de cor com modelos de pesos abertos</a>: criar e revisar propostas de cor, enquanto a digitalização continua sendo a referência principal.</li>
    <li><a href="{{ '/training-inference-review/' | relative_url }}">Treinamento, inferência e revisão</a>: preparar o material, iterar e decidir quando um resultado é aceitável.</li>
    <li><a href="{{ '/open-weight-color-recovery/research-routes/' | relative_url }}">Caminhos de pesquisa e questões em aberto</a>: um retrato anterior da pesquisa, com as suas evidências e limitações.</li>
    <li><a href="{{ '/' | relative_url }}">Toda a pesquisa deste site</a>, ou o <a href="https://github.com/fabiocolor/custom-machine-learning-for-film-restoration">repositório no GitHub</a>.</li>
  </ul>
</section>

<section class="fc-thanks" id="thanks">
  <p class="fc-slide fc-slide-light">Slide 23</p>
  <h2 id="thanks-title">Obrigado</h2>
  <p>Obrigado à FIAT/IFTA e aos organizadores. Um agradecimento especial:</p>
  <ul>
    <li>à Studiocanal, por <em>For Better, For Worse</em> (1954) e <em>Poison Pen</em> (1939)</li>
    <li>ao George Eastman Museum, por <em>Knight of the Trail</em> (1915)</li>
  </ul>
  <p class="fc-small">Os outros exemplos são testes de pesquisa feitos com cópias disponíveis publicamente, em sua maioria trailers desbotados do archive.org. Os trechos dos filmes continuam sendo propriedade dos seus detentores de direitos, e mostrá-los aqui não dá permissão para reutilizá-los. Veja os <a href="{{ '/credits/' | relative_url }}">créditos e atribuições</a>.</p>
  <p>Perguntas e sugestões são bem-vindas:</p>
  <ul>
    <li>E-mail: <a href="mailto:info@fabiocolor.com">info@fabiocolor.com</a></li>
    <li>LinkedIn: <a href="https://www.linkedin.com/in/fabiobedoya/">/fabiobedoya</a> · Instagram: <a href="https://www.instagram.com/fabiocolor/">@fabiocolor</a></li>
    <li>YouTube: <a href="https://www.youtube.com/@fabiocolor">@fabiocolor</a> · GitHub: <a href="https://github.com/fabiocolor">/fabiocolor</a></li>
  </ul>
</section>

</div>

{% include fiat-companion/script.html %}
