from .tree import Node

def serialize_tree(root: Node) -> str:
    """
    Gera uma representação visual (textual/ASCII) da árvore de Huffman.
    Isso atende ao requisito de 'formato textual' e facilita a correção.
    """
    if not root:
        return "Árvore vazia"

    lines = []

    def _build_visual(node: Node, prefix: str, is_left: bool, is_root: bool):
        if is_root:
            # A raiz mostra a frequência total do texto
            lines.append(f"[RAIZ] (Total: {node.freq})")
        else:
            # Define o conector: ├── para filhos esquerdos/meio, └── para o último
            connector = "├── " if is_left else "└── "
            
            # Bit do caminho: 0 para esquerda, 1 para direita
            path_bit = "0" if is_left else "1"
            
            content = ""
            if node.is_leaf():
                # Se for folha, mostra a palavra e a frequência
                content = f"'{node.word}' ({node.freq})"
            else:
                # Se for nó interno, mostra apenas a soma das frequências
                content = f"[{node.freq}]"
                
            lines.append(f"{prefix}{connector}{path_bit}: {content}")

        # Prepara o prefixo para o próximo nível
        if is_root:
            new_prefix = ""
        else:
            # Se este nó for 'left' (├──), a linha vertical continua descendo (│)
            # Se for 'right' (└──), o espaço fica vazio ( )
            new_prefix = prefix + ("│   " if is_left else "    ")

        # Recursão (Travessia Pré-ordem)
        if not node.is_leaf():
            # Importante: Huffman é árvore cheia (sempre tem 2 filhos ou nenhum),
            # mas por segurança checamos.
            # O filho da esquerda (0) passamos is_left=True
            if node.left:
                _build_visual(node.left, new_prefix, is_left=True, is_root=False)
            # O filho da direita (1) passamos is_left=False (fecha o galho)
            if node.right:
                _build_visual(node.right, new_prefix, is_left=False, is_root=False)

    # Inicia a construção
    _build_visual(root, "", is_left=False, is_root=True)
    return "\n".join(lines)