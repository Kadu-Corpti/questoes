<?php
/**
 * name: simulado_visual.php
 * Finalidade: Estudo Intensivo com Suporte a Diagramas.
 */

$questoes = [
    1 => [
        'p' => "Analise o diagrama de estados de um Autômato Finito (AFD). Se o estado inicial possui uma transição com '0' para si mesmo e com '1' para um estado final, qual linguagem ele reconhece?",
        'o' => ['A'=>"Palavras que começam com 0", 'B'=>"Palavras que terminam com 1", 'C'=>"Palavras com número par de 0s", 'D'=>"Apenas a palavra vazia"],
        'c' => 'B',
        'img' => 'diagrama_afd_1.png', // Coloque o nome do seu arquivo aqui
        'e' => "Em diagramas, o loop no estado inicial indica que o símbolo pode se repetir, e a transição para o estado final define a condição de aceitação."
    ],
    2 => [
        'p' => "Em uma Máquina de Turing, a transição representada no diagrama como (a, b, R) significa:",
        'o' => ['A'=>"Lê 'a', grava 'b' e move o cabeçote para a direita", 'B'=>"Lê 'b', grava 'a' e move para a direita", 'C'=>"Se o estado for 'a', mude para 'b'", 'D'=>"Mova para a direita apenas se a fita estiver vazia"],
        'c' => 'A',
        'img' => 'transicao_mt.png',
        'e' => "A notação padrão em diagramas de MT segue a ordem: Símbolo Lido / Símbolo Gravado / Direção do Movimento."
    ],
    3 => [
        'p' => "Qual das funções abaixo cresce mais rapidamente no gráfico de complexidade assintótica?",
        'o' => ['A'=>"f(n) = n log n", 'B'=>"f(n) = n²", 'C'=>"f(n) = 2^n", 'D'=>"f(n) = n!"],
        'c' => 'D',
        'img' => 'grafico_complexidade.png',
        'e' => "O crescimento fatorial O(n!) ultrapassa o exponencial O(2^n) rapidamente."
    ],
    // Adicione as outras 37 questões seguindo este padrão...
];

$feedback = "";
$status = "";
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $id = (int)$_POST['id'];
    $r = $_POST['res'] ?? '';
    if ($r === $questoes[$id]['c']) {
        $feedback = "<strong>Correto!</strong> " . $questoes[$id]['e'];
        $status = "success";
    } else {
        $feedback = "<strong>Errado.</strong> A correta é " . $questoes[$id]['c'] . ". " . $questoes[$id]['e'];
        $status = "error";
    }
}
?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Simulado com Diagramas</title>
    <style>
        :root { --primary: #2563eb; --bg: #ffffff; --card-bg: #f8fafc; }
        body { font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background: var(--bg); color: #1e293b; line-height: 1.6; padding: 20px; }
        .wrapper { max-width: 800px; margin: auto; }
        .card { background: var(--card-bg); border-radius: 12px; padding: 25px; margin-bottom: 30px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }
        .q-img { max-width: 100%; height: auto; display: block; margin: 15px 0; border-radius: 8px; border: 1px solid #cbd5e1; background: #fff; }
        .option { display: block; background: #fff; padding: 15px; border-radius: 8px; margin-bottom: 10px; cursor: pointer; border: 1px solid #e2e8f0; transition: 0.2s; }
        .option:hover { border-color: var(--primary); background: #eff6ff; }
        button { background: var(--primary); color: white; border: none; padding: 12px; border-radius: 8px; font-weight: bold; cursor: pointer; width: 100%; margin-top: 10px; }
        .feedback { padding: 20px; border-radius: 10px; margin-bottom: 25px; font-weight: 500; }
        .success { background: #dcfce7; color: #166534; border: 1px solid #bbf7d0; }
        .error { background: #fee2e2; color: #991b1b; border: 1px solid #fecaca; }
    </style>
</head>
<body>
    <div class="wrapper">
        <h1>Simulado Visual: Computabilidade</h1>
        
        <?php if ($feedback): ?>
            <div class="feedback <?= $status ?>"><?= $feedback ?></div>
        <?php endif; ?>

        <?php foreach ($questoes as $id => $q): ?>
        <div class="card" id="q<?= $id ?>">
            <strong>Questão <?= $id ?>:</strong><br>
            <?= htmlspecialchars($q['p']) ?>
            
            <?php if (!empty($q['img']) && file_exists($q['img'])): ?>
                <img src="<?= $q['img'] ?>" alt="Diagrama da questão" class="q-img">
            <?php else: ?>
                <div style="font-size: 0.8em; color: #94a3b8; margin: 10px 0;">[Espaço para diagrama: <?= $q['img'] ?>]</div>
            <?php endif; ?>

            <form method="POST" action="#q<?= $id ?>">
                <input type="hidden" name="id" value="<?= $id ?>">
                <?php foreach ($q['o'] as $letra => $txt): ?>
                    <label class="option">
                        <input type="radio" name="res" value="<?= $letra ?>" required>
                        <strong><?= $letra ?>)</strong> <?= htmlspecialchars($txt) ?>
                    </label>
                <?php endforeach; ?>
                <button type="submit">Verificar Resposta</button>
            </form>
        </div>
        <?php endforeach; ?>
    </div>
</body>
</html>
