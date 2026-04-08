<?php
/**
 * name: simulado.php
 * Simulado de Análise de Computabilidade e Complexidade
 * Baseado no conteúdo da Profa. Regina Fedozzi [cite: 1, 4]
 */

$questoes = [
    // --- COMPLEXIDADE E BIG O  ---
    1 => ['p' => "Na análise assintótica, se um algoritmo possui complexidade $f(n) = 2n^2 + 50n + 100$, qual sua notação Big O?", 'o' => ['A'=>"O(n)", 'B'=>"O(n^2)", 'C'=>"O(50n)", 'D'=>"O(1)"], 'c' => 'B', 'e' => "Ignoramos constantes e termos de menor grau."],
    2 => ['p' => "Qual a complexidade de tempo da Busca Binária?", 'o' => ['A'=>"O(n)", 'B'=>"O(n log n)", 'C'=>"O(log n)", 'D'=>"O(1)"], 'c' => 'C', 'e' => "A cada passo o problema é dividido ao meio (dividir para conquistar)."],
    3 => ['p' => "A complexidade $O(1)$ indica que o tempo de execução:", 'o' => ['A'=>"Aumenta linearmente com n", 'B'=>"É fixo, independente do tamanho da entrada", 'C'=>"Cresce logaritmicamente", 'D'=>"Dobra a cada novo elemento"], 'c' => 'B', 'e' => "O tempo é constante e independe do tamanho da entrada."],
    4 => ['p' => "Qual destas ordens de crescimento é a MENOS eficiente para grandes valores de n?", 'o' => ['A'=>"O(n log n)", 'B'=>"O(n^3)", 'C'=>"O(2^n)", 'D'=>"O(n!)"], 'c' => 'D', 'e' => "O crescimento fatorial $O(n!)$ ultrapassa o exponencial rapidamente."],
    5 => ['p' => "O algoritmo MinMax (Caso 3) utiliza qual estratégia para ser o mais eficiente?", 'o' => ['A'=>"Busca linear simples", 'B'=>"Comparação par-a-par", 'C'=>"Ordenação prévia do vetor", 'D'=>"Recursão múltipla"], 'c' => 'B', 'e' => "Realiza aproximadamente $3n/2$ comparações."],
    6 => ['p' => "Qual a complexidade de um algoritmo com dois laços 'for' aninhados indo de 1 até n?", 'o' => ['A'=>"O(2n)", 'B'=>"O(n^2)", 'C'=>"O(n)", 'D'=>"O(log n)"], 'c' => 'B', 'e' => "A iteração de um laço dentro do outro resulta em $n \times n$."],
    7 => ['p' => "Um algoritmo $O(n)$ é considerado:", 'o' => ['A'=>"Constante", 'B'=>"Linear", 'C'=>"Quadrático", 'D'=>"Exponencial"], 'c' => 'B', 'e' => "O tempo cresce na mesma proporção que a entrada."],
    8 => ['p' => "O termo 'assintótico' refere-se ao comportamento do algoritmo quando:", 'o' => ['A'=>"n tende ao infinito", 'B'=>"n é igual a zero", 'C'=>"O código possui erros", 'D'=>"A memória acaba"], 'c' => 'A', 'e' => "Analisamos o limite de crescimento para entradas grandes[cite: 7]."],

    // --- AUTÔMATOS E LINGUAGENS [cite: 3] ---
    9 => ['p' => "Um Autômato Finito Determinístico (AFD) é definido por uma 5-tupla. O que representa o símbolo $\Sigma$?", 'o' => ['A'=>"Conjunto de estados", 'B'=>"Função de transição", 'C'=>"Alfabeto de entrada", 'D'=>"Estado inicial"], 'c' => 'C', 'e' => "Sigma é o alfabeto finito de símbolos[cite: 3]."],
    10 => ['p' => "A palavra vazia em linguagens formais é representada por:", 'o' => ['A'=>"Ø", 'B'=>"$\epsilon$ (Epsilon)", 'C'=>"$\Sigma$", 'D'=>"Infinity"], 'c' => 'B', 'e' => "Epsilon denota uma string de comprimento zero[cite: 3]."],
    11 => ['p' => "Qual a principal característica da Máquina de Mealy?", 'o' => ['A'=>"A saída depende apenas do estado atual", 'B'=>"A saída depende do estado atual e da entrada", 'C'=>"Não possui estados finais", 'D'=>"É infinita"], 'c' => 'B', 'e' => "Diferente da máquina de Moore, Mealy associa a saída às transições[cite: 6]."],
    12 => ['p' => "Em um diagrama de estados, o círculo duplo representa:", 'o' => ['A'=>"Estado Inicial", 'B'=>"Estado Final/Aceitação", 'C'=>"Erro", 'D'=>"Loop Infinito"], 'c' => 'B', 'e' => "Indica que a palavra foi processada e aceita[cite: 3]."],
    13 => ['p' => "O que é o fecho de Kleene ($\Sigma^*$)?", 'o' => ['A'=>"Apenas palavras binárias", 'B'=>"Conjunto de todas as palavras possíveis, incluindo a vazia", 'C'=>"Palavras de tamanho fixo", 'D'=>"Apenas a palavra vazia"], 'c' => 'B', 'e' => "Representa o fechamento reflexivo sobre o alfabeto[cite: 3]."],
    14 => ['p' => "Linguagens reconhecidas por AFDs são chamadas de:", 'o' => ['A'=>"Linguagens Humanas", 'B'=>"Linguagens Regulares", 'C'=>"Linguagens Sensíveis", 'D'=>"Linguagens de Máquina"], 'c' => 'B', 'e' => "AFDs e AFNs reconhecem a classe das linguagens regulares[cite: 7]."],
    15 => ['p' => "Dada a transição $\delta(q0, 1) = q1$, o que ocorre?", 'o' => ['A'=>"A máquina para", 'B'=>"No estado q0, ao ler 1, vai para q1", 'C'=>"A máquina grava 1 na fita", 'D'=>"O estado inicial muda"], 'c' => 'B', 'e' => "É a função de mapeamento de estados e símbolos[cite: 3]."],
    16 => ['p' => "A Máquina de Moore associa sua saída a:", 'o' => ['A'=>"Transições", 'B'=>"Estados", 'C'=>"Alfabeto", 'D'=>"Entrada externa"], 'c' => 'B', 'e' => "A saída depende unicamente do estado em que a máquina se encontra[cite: 6]."],

    // --- MÁQUINA DE TURING [cite: 5] ---
    17 => ['p' => "A Máquina de Turing (MT) é definida por uma 7-upla. O que é o símbolo 'b' ou '# '?", 'o' => ['A'=>"Símbolo de início", 'B'=>"Símbolo branco (fita vazia)", 'C'=>"Símbolo de erro", 'D'=>"Estado final"], 'c' => 'B', 'e' => "Indica que a célula da fita não contém dados de entrada[cite: 5]."],
    18 => ['p' => "Diferente de um AFD, a Máquina de Turing pode:", 'o' => ['A'=>"Apenas ler", 'B'=>"Ler e gravar na fita", 'C'=>"Apenas mover para a direita", 'D'=>"Ter estados infinitos"], 'c' => 'B', 'e' => "A MT possui cabeçote de leitura/escrita bidirecional[cite: 5]."],
    19 => ['p' => "O que afirma a Tese de Church-Turing?", 'o' => ['A'=>"Computadores são infinitos", 'B'=>"A MT define formalmente o que é um algoritmo computável", 'C'=>"Todo algoritmo é linear", 'D'=>"O Problema da Parada tem solução"], 'c' => 'B', 'e' => "Estabelece que qualquer função computável pode ser calculada por uma MT[cite: 2, 7]."],
    20 => ['p' => "Uma MT que sempre para (aceitando ou rejeitando) é chamada de:", 'o' => ['A'=>"Reconhecedora", 'B'=>"Decisora", 'C'=>"Recursiva", 'D'=>"Infinita"], 'c' => 'B', 'e' => "Um decisor nunca entra em loop para nenhuma entrada[cite: 7]."],
    21 => ['p' => "Aumentar o número de fitas em uma MT:", 'o' => ['A'=>"Aumenta o poder computacional", 'B'=>"Não aumenta o poder, apenas a eficiência prática", 'C'=>"Torna a máquina indecidível", 'D'=>"Permite ler linguagens humanas"], 'c' => 'B', 'e' => "MTs com múltiplas fitas são equivalentes à MT padrão de fita única[cite: 6]."],
    22 => ['p' => "A transição $(a, b, R)$ em uma MT significa:", 'o' => ['A'=>"Lê a, grava b, move para Direita", 'B'=>"Lê b, grava a, move para Direita", 'C'=>"Estado a para estado b", 'D'=>"Erro de leitura"], 'c' => 'A', 'e' => "Símbolo Lido / Símbolo Gravado / Movimento[cite: 5]."],
    23 => ['p' => "O Problema da Parada (Halting Problem) é:", 'o' => ['A'=>"Decidível", 'B'=>"Indecidível", 'C'=>"Linear", 'D'=>"Constante"], 'c' => 'B', 'e' => "Provado por Turing: não há algoritmo que determine se qualquer programa para[cite: 7]."],
    24 => ['p' => "Uma linguagem é Turing-reconhecível se for:", 'o' => ['A'=>"Recursiva", 'B'=>"Recursivamente Enumerável", 'C'=>"Linguagem Regular", 'D'=>"Ambígua"], 'c' => 'B', 'e' => "Existe uma MT que aceita todas as strings da linguagem[cite: 7]."],

    // --- DECIDIBILIDADE E RECURSIVIDADE [cite: 4, 7] ---
    25 => ['p' => "Quem provou os Teoremas da Incompletude em 1931?", 'o' => ['A'=>"Alan Turing", 'B'=>"Kurt Gödel", 'C'=>"David Hilbert", 'D'=>"Georg Cantor"], 'c' => 'B', 'e' => "Gödel mostrou que sistemas formais consistentes são incompletos[cite: 2]."],
    26 => ['p' => "O que é o Problema da Aceitação ($A_{MT}$)?", 'o' => ['A'=>"Verificar se uma MT aceita uma string w", 'B'=>"Contar estados de uma MT", 'C'=>"Verificar se a MT tem fita infinita", 'D'=>"Mudar o alfabeto"], 'c' => 'A', 'e' => "É um problema indecidível, mas Turing-reconhecível[cite: 7]."],
    27 => ['p' => "A técnica de Diagonalização de Cantor serve para:", 'o' => ['A'=>"Somar matrizes", 'B'=>"Comparar o tamanho de conjuntos infinitos", 'C'=>"Reduzir o código", 'D'=>"Gerar números aleatórios"], 'c' => 'B', 'e' => "Usada para provar a incontabilidade dos números reais e a indecidibilidade[cite: 7]."],
    28 => ['p' => "Se o Problema A se reduz ao Problema B ($A \le B$) e B é decidível:", 'o' => ['A'=>"A é impossível", 'B'=>"A também é decidível", 'C'=>"A é indecidível", 'D'=>"Nada se conclui"], 'c' => 'B', 'e' => "A solução de B pode ser usada para resolver A[cite: 7]."],
    29 => ['p' => "Um problema é dito 'Indecidível' quando:", 'o' => ['A'=>"Não tem resposta", 'B'=>"Não existe um algoritmo universal de decisão", 'C'=>"A resposta é 'Talvez'", 'D'=>"Leva muito tempo para processar"], 'c' => 'B', 'e' => "Nenhuma MT pode dar 'Sim' ou 'Não' para todos os casos em tempo finito[cite: 7]."],
    30 => ['p' => "O Teorema da Recursão garante que:", 'o' => ['A'=>"O código nunca para", 'B'=>"Uma MT pode obter e usar sua própria descrição/código", 'C'=>"AFDs são iguais a MTs", 'D'=>"Tudo é decidível"], 'c' => 'B', 'e' => "Permite programas autorreferenciados (como vírus ou quines)[cite: 7]."],
    31 => ['p' => "O caso base em uma função recursiva serve para:", 'o' => ['A'=>"Reiniciar o computador", 'B'=>"Interromper a recursão e evitar loop infinito", 'C'=>"Multiplicar o valor", 'D'=>"Chamar a função novamente"], 'c' => 'B', 'e' => "Define a instância mínima resolvida diretamente."],
    32 => ['p' => "A complexidade da Torre de Hanói com n discos é:", 'o' => ['A'=>"$O(n)$", 'B'=>"$O(n^2)$", 'C'=>"$O(2^n)$", 'D'=>"$O(log n)$"], 'c' => 'C', 'e' => "O número de movimentos é $2^n - 1$."],
    33 => ['p' => "Qual a complexidade de espaço (pilha) do fatorial recursivo?", 'o' => ['A'=>"$O(1)$", 'B'=>"$O(n)$", 'C'=>"$O(n^2)$", 'D'=>"$O(2^n)$"], 'c' => 'B', 'e' => "Cada chamada recursiva ocupa um espaço na pilha de execução."],
    34 => ['p' => "O algoritmo QuickSort tem complexidade média de:", 'o' => ['A'=>"$O(n)$", 'B'=>"$O(n log n)$", 'C'=>"$O(n^2)$", 'D'=>"$O(1)$"], 'c' => 'B', 'e' => "É a complexidade padrão de algoritmos eficientes de ordenação."],
    35 => ['p' => "O Problema de Decisão aceita quais respostas?", 'o' => ['A'=>"Sim ou Não", 'B'=>"Números reais", 'C'=>"Strings infinitas", 'D'=>"Apenas números pares"], 'c' => 'A', 'e' => "A resposta deve ser binária e definitiva[cite: 7]."],
    36 => ['p' => "Linguagens Recursivas são aquelas em que a MT:", 'o' => ['A'=>"Nunca para", 'B'=>"Sempre para (Decidíveis)", 'C'=>"Só aceita zeros", 'D'=>"Entra em loop"], 'c' => 'B', 'e' => "São o subconjunto decidível das linguagens reconhecíveis[cite: 7]."],
    37 => ['p' => "O que ocorre se uma recursão não tiver caso base?", 'o' => ['A'=>"O programa fica rápido", 'B'=>"Estouro de pilha (Stack Overflow)", 'C'=>"O resultado é zero", 'D'=>"A memória aumenta"], 'c' => 'B', 'e' => "As chamadas empilham infinitamente até travar o sistema."],
    38 => ['p' => "A Conjectura de Collatz ($3x+1$) é famosa por:", 'o' => ['A'=>"Ser muito fácil", 'B'=>"Não ter prova de decidibilidade até hoje", 'C'=>"Ter sido provada por Turing", 'D'=>"Só funcionar para números pares"], 'c' => 'B', 'e' => "Se o Problema da Parada fosse decidível, saberíamos se ela para para todo n[cite: 7]."],
    39 => ['p' => "Qual a complexidade de calcular o n-ésimo termo de Fibonacci recursivamente (simples)?", 'o' => ['A'=>"$O(n)$", 'B'=>"$O(log n)$", 'C'=>"$O(2^n)$", 'D'=>"$O(n^2)$"], 'c' => 'C', 'e' => "Gera uma árvore de chamadas exponencial."],
    40 => ['p' => "O Teorema da Incompletude de Gödel afirma que:", 'o' => ['A'=>"Tudo pode ser provado", 'B'=>"Existem sentenças verdadeiras que não podem ser provadas num sistema formal", 'C'=>"Computadores são perfeitos", 'D'=>"AFDs são melhores que MTs"], 'c' => 'B', 'e' => "Estabelece os limites fundamentais da lógica e computação[cite: 2]."],
];

// Lógica de Processamento
$feedback = ""; $status = ""; $resp_correta = ""; $q_id = 0;
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $q_id = (int)$_POST['id'];
    $r_usr = $_POST['res'] ?? '';
    $correta = $questoes[$q_id]['c'];
    if ($r_usr === $correta) {
        $feedback = "<strong>Correto!</strong> " . $questoes[$q_id]['e'];
        $status = "success";
    } else {
        $feedback = "<strong>Errado!</strong> A correta é a <b>$correta</b>. " . $questoes[$q_id]['e'];
        $status = "error";
    }
}
?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MasterSimulado CC 2026</title>
    <style>
        :root { --primary: #2563eb; --bg: #f1f5f9; --card: #ffffff; --text: #1e293b; }
        body { font-family: 'Inter', -apple-system, system-ui, sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; padding: 20px; }
        .container { max-width: 800px; margin: auto; }
        h1 { text-align: center; color: var(--primary); font-weight: 800; margin-bottom: 40px; }
        .card { background: var(--card); border-radius: 16px; padding: 30px; margin-bottom: 25px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; }
        .q-title { font-size: 1.2rem; font-weight: 700; margin-bottom: 20px; display: block; border-left: 4px solid var(--primary); padding-left: 15px; }
        .q-img-placeholder { background: #f8fafc; border: 2px dashed #cbd5e1; height: 150px; display: flex; align-items: center; justify-content: center; border-radius: 12px; margin: 15px 0; color: #94a3b8; font-size: 0.9rem; }
        .option { display: block; background: #f8fafc; padding: 15px 20px; border-radius: 12px; margin-bottom: 10px; cursor: pointer; border: 2px solid transparent; transition: 0.2s; }
        .option:hover { border-color: var(--primary); background: #eff6ff; }
        input[type="radio"] { margin-right: 12px; transform: scale(1.2); }
        button { background: var(--primary); color: white; border: none; padding: 14px; border-radius: 12px; font-weight: 700; cursor: pointer; width: 100%; font-size: 1rem; margin-top: 10px; box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.2); }
        .alert { padding: 20px; border-radius: 12px; margin-bottom: 20px; font-weight: 500; border: 1px solid transparent; }
        .success { background: #dcfce7; color: #166534; border-color: #bbf7d0; }
        .error { background: #fee2e2; color: #991b1b; border-color: #fecaca; }
        .nav-anchor { scroll-margin-top: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Simulado Visual: Computabilidade</h1>
        
        <?php if ($feedback): ?>
            <div class="alert <?= $status ?>"><?= $feedback ?></div>
        <?php endif; ?>

        <?php foreach ($questoes as $id => $q): ?>
        <div class="card nav-anchor" id="q<?= $id ?>">
            <span class="q-title">Questão <?= $id ?></span>
            <p><?= htmlspecialchars($q['p']) ?></p>
            
            <?php 
            $foto = "foto_q{$id}.png"; 
            if (file_exists($foto)): ?>
                <img src="<?= $foto ?>" style="max-width:100%; border-radius:12px; margin-bottom:15px;">
            <?php else: ?>
                <div class="q-img-placeholder">[Arraste a foto "foto_q<?= $id ?>.png" para a pasta do script para vê-la aqui]</div>
            <?php endif; ?>

            <form method="POST" action="#q<?= $id ?>">
                <input type="hidden" name="id" value="<?= $id ?>">
                <?php foreach ($q['o'] as $letra => $txt): ?>
                    <label class="option">
                        <input type="radio" name="res" value="<?= $letra ?>" required <?= ($q_id == $id && $r_usr == $letra) ? 'checked' : '' ?>>
                        <strong><?= $letra ?>)</strong> <?= htmlspecialchars($txt) ?>
                    </label>
                <?php endforeach; ?>
                <button type="submit">Verificar Resposta</button>
            </form>
        </div>
        <?php endforeach; ?>
        
        <p style="text-align: center; color: #94a3b8; padding: 40px;">Bons estudos para a prova! 🚀</p>
    </div>
</body>
</html>
