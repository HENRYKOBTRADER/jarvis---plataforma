<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>JARVIS — Plataforma</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=Rajdhani:wght@300;400;500;600;700&family=Share+Tech+Mono&display=swap" rel="stylesheet">
<style>
  :root{
    --bg:#02060d;--ciano:#3ad6ff;--ciano-soft:#7fe7ff;--gold:#ffcf6b;
    --line:rgba(58,214,255,.18);--glow:0 0 12px rgba(58,214,255,.55);
    --warn:#ff6b6b;
  }
  *{margin:0;padding:0;box-sizing:border-box}
  body{background:var(--bg);color:#cfeefb;font-family:'Rajdhani',sans-serif;min-height:100vh;overflow-x:hidden}
  body::before{content:"";position:fixed;inset:0;z-index:0;pointer-events:none;
    background:
      radial-gradient(ellipse at 50% 0%, rgba(58,214,255,.08), transparent 55%),
      linear-gradient(transparent 0 2px, var(--line) 2px 3px) 0 0/100% 46px,
      linear-gradient(90deg, transparent 0 2px, var(--line) 2px 3px) 0 0/46px 100%;
    opacity:.4;mask:radial-gradient(ellipse at 50% 30%, #000 40%, transparent 90%)}

  header{position:relative;z-index:5;display:flex;justify-content:space-between;
    align-items:center;padding:20px 36px;border-bottom:1px solid var(--line)}
  .brand{display:flex;align-items:center;gap:12px}
  .brand .mark{width:28px;height:28px;border-radius:50%;border:1.5px solid var(--ciano);
    box-shadow:var(--glow),inset 0 0 6px rgba(58,214,255,.4);position:relative}
  .brand .mark::after{content:"";position:absolute;inset:10px;border-radius:50%;
    background:var(--ciano);box-shadow:var(--glow)}
  .brand h1{font-family:'Orbitron',sans-serif;font-weight:700;font-size:.9rem;letter-spacing:.3em;color:#eafaff}
  header a{color:#8fcadf;text-decoration:none;font-family:'Share Tech Mono',monospace;
    font-size:.74rem;letter-spacing:.15em;text-transform:uppercase;transition:.25s}
  header a:hover{color:var(--ciano);text-shadow:var(--glow)}

  .wrap{position:relative;z-index:5;max-width:1180px;margin:0 auto;padding:34px 30px 80px}
  .titlebar{display:flex;justify-content:space-between;align-items:flex-end;
    margin-bottom:28px;flex-wrap:wrap;gap:14px}
  .titlebar h2{font-family:'Orbitron',sans-serif;font-weight:500;font-size:1.4rem;
    letter-spacing:.1em;color:#eafaff}
  .conn{font-family:'Share Tech Mono',monospace;font-size:.74rem;letter-spacing:.12em;
    display:flex;align-items:center;gap:8px;padding:8px 14px;border:1px solid var(--line)}
  .conn .dot{width:8px;height:8px;border-radius:50%;background:#5f93a8;transition:.3s}
  .conn.live .dot{background:var(--ciano);box-shadow:var(--glow);animation:pulse 1.5s infinite}
  @keyframes pulse{0%,100%{opacity:1}50%{opacity:.3}}

  .grid{display:grid;grid-template-columns:1.3fr 1fr;gap:22px}
  .panel{border:1px solid var(--line);background:rgba(4,11,22,.55);position:relative;
    clip-path:polygon(0 0,calc(100% - 14px) 0,100% 14px,100% 100%,14px 100%,0 calc(100% - 14px))}
  .panel-h{padding:14px 20px;border-bottom:1px solid var(--line);
    font-family:'Share Tech Mono',monospace;font-size:.74rem;letter-spacing:.2em;
    text-transform:uppercase;color:var(--ciano);display:flex;justify-content:space-between;align-items:center}
  .panel-b{padding:22px 20px}

  /* leitura de dados */
  .reading{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}
  .metric{border:1px solid var(--line);padding:16px 18px;background:rgba(58,214,255,.03);position:relative}
  .metric .k{font-family:'Share Tech Mono',monospace;font-size:.68rem;letter-spacing:.15em;
    color:#7fb4c7;text-transform:uppercase}
  .metric .v{font-family:'Orbitron',sans-serif;font-weight:700;font-size:1.7rem;
    color:#eafaff;margin-top:6px;text-shadow:0 0 14px rgba(58,214,255,.4)}
  .metric .v.idle{color:#3f6678;text-shadow:none}

  /* núcleo lateral */
  .corebox{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px;padding:30px 20px}
  .mini-core{width:140px;height:140px;position:relative;display:flex;align-items:center;justify-content:center}
  .mini-core .rg{position:absolute;border-radius:50%;border:1px solid var(--ciano);opacity:.7}
  .mini-core .rg.a{inset:0;border-top-color:transparent;animation:spin 9s linear infinite}
  .mini-core .rg.b{inset:24px;border-left-color:transparent;animation:spin 6s linear infinite reverse}
  @keyframes spin{to{transform:rotate(360deg)}}
  .mini-core .cc{width:54px;height:54px;border-radius:50%;
    background:radial-gradient(circle,#bff3ff,var(--ciano) 50%,#0a7fa8);
    box-shadow:0 0 30px rgba(58,214,255,.6);animation:breathe 3.5s ease-in-out infinite}
  @keyframes breathe{0%,100%{transform:scale(1)}50%{transform:scale(1.08)}}
  .ia-status{text-align:center;font-family:'Share Tech Mono',monospace;font-size:.74rem;letter-spacing:.12em}
  .ia-status .big{display:block;font-size:.95rem;margin-bottom:6px;color:var(--gold)}
  .ia-status.on .big{color:var(--ciano)}

  .analise{margin-top:22px}
  .analise .box{border:1px solid var(--line);padding:18px;min-height:120px;
    font-weight:300;line-height:1.6;color:#a9d6e8;background:rgba(4,11,22,.4);white-space:pre-wrap}
  .analise .box.idle{color:#557585;font-style:italic}

  .hint{margin-top:26px;padding:18px 20px;border:1px dashed rgba(255,207,107,.35);
    background:rgba(255,207,107,.04);font-size:.92rem;font-weight:300;line-height:1.6;color:#d8c79e}
  .hint b{color:var(--gold);font-weight:600}
  code{font-family:'Share Tech Mono',monospace;font-size:.85em;color:var(--ciano-soft);
    background:rgba(58,214,255,.08);padding:2px 7px}

  @media(max-width:820px){.grid{grid-template-columns:1fr}.reading{grid-template-columns:repeat(2,1fr)}}
  @media(max-width:480px){.reading{grid-template-columns:1fr}}
</style>
</head>
<body>
  <header>
    <div class="brand"><div class="mark"></div><h1>J·A·R·V·I·S</h1></div>
    <a href="/">← Voltar ao núcleo</a>
  </header>

  <div class="wrap">
    <div class="titlebar">
      <h2>Plataforma de Fluxo</h2>
      <div class="conn" id="conn"><span class="dot"></span><span id="connTxt">AGUARDANDO SENSOR</span></div>
    </div>

    <div class="grid">
      <!-- LEITURA -->
      <div class="panel">
        <div class="panel-h"><span>Leitura do Sensor</span><span id="sym">— —</span></div>
        <div class="panel-b">
          <div class="reading" id="reading">
            <div class="metric"><div class="k">CVD Z-Score</div><div class="v idle" data-k="cvd_zscore">—</div></div>
            <div class="metric"><div class="k">Semi-Variância</div><div class="v idle" data-k="semi_variancia">—</div></div>
            <div class="metric"><div class="k">Aceleração</div><div class="v idle" data-k="aceleracao">—</div></div>
            <div class="metric"><div class="k">Volume Δ</div><div class="v idle" data-k="volume_delta">—</div></div>
          </div>
        </div>
      </div>

      <!-- NÚCLEO -->
      <div class="panel">
        <div class="panel-h"><span>Núcleo</span><span id="ts">—</span></div>
        <div class="panel-b corebox">
          <div class="mini-core">
            <div class="rg a"></div><div class="rg b"></div><div class="cc"></div>
          </div>
          <div class="ia-status {% if ia_ativa %}on{% endif %}" id="iaStatus">
            <span class="big">{% if ia_ativa %}IA ATIVA{% else %}IA EM STANDBY{% endif %}</span>
            {% if ia_ativa %}núcleo conectado{% else %}aguardando chave da API{% endif %}
          </div>
        </div>
      </div>
    </div>

    <!-- ANÁLISE -->
    <div class="panel analise">
      <div class="panel-h"><span>Análise do Núcleo</span></div>
      <div class="panel-b">
        <div class="box idle" id="analiseBox">A análise aparecerá aqui quando a IA estiver ativa e o sensor enviar dados.</div>
      </div>
    </div>

    <div class="hint">
      <b>Como ligar o sensor:</b> no seu EA leitor (MQL5), envie os dados via
      <code>WebRequest()</code> para <code>/api/leitura</code> em formato JSON.
      A plataforma lê esse fluxo automaticamente a cada 3 segundos.
      Para ligar a IA, adicione a variável <code>ANTHROPIC_API_KEY</code> no painel do Render.
    </div>
  </div>

  <script>
    const conn=document.getElementById('conn'), connTxt=document.getElementById('connTxt');
    const sym=document.getElementById('sym'), ts=document.getElementById('ts');
    const box=document.getElementById('analiseBox');

    function fmt(n){return (typeof n==='number')? n.toFixed(2) : n;}

    async function poll(){
      try{
        const r=await fetch('/api/estado');
        const d=await r.json();
        if(d.timestamp){
          conn.classList.add('live'); connTxt.textContent='SENSOR ATIVO';
          sym.textContent=d.simbolo||'—';
          ts.textContent=new Date(d.timestamp*1000).toLocaleTimeString('pt-BR');
          document.querySelectorAll('.metric .v').forEach(el=>{
            const k=el.dataset.k, val=d.dados?.[k];
            if(val!==undefined){el.textContent=fmt(val);el.classList.remove('idle');}
          });
          if(d.analise_claude){box.textContent=d.analise_claude;box.classList.remove('idle');}
        }else{
          conn.classList.remove('live'); connTxt.textContent='AGUARDANDO SENSOR';
        }
      }catch(e){ connTxt.textContent='ERRO DE CONEXÃO'; }
    }
    poll(); setInterval(poll,3000);
  </script>
</body>
</html>
