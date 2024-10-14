import yaml
from graphviz import Digraph

import os
current_dir = os.path.dirname(os.path.abspath(__file__))

def visualize_flow(yaml_file):
    # YAML 파일 읽기
    with open(yaml_file, 'r') as file:
        flow_data = yaml.safe_load(file)

    # Graphviz 객체 생성
    dot = Digraph(comment='Prompt Flow')
    dot.attr(rankdir='TB', size='8,8')

    # 노드 추가
    if 'nodes' in flow_data:
        for node in flow_data['nodes']:
            node_name = node.get('name', '')
            node_type = node.get('type', '')
            dot.node(node_name, f"{node_name}\n({node_type})")

    # 엣지 추가 (노드 간 연결)
    if 'nodes' in flow_data:
        for node in flow_data['nodes']:
            node_name = node.get('name', '')
            if 'inputs' in node:
                for input_key, input_value in node['inputs'].items():
                    if isinstance(input_value, str) and input_value.startswith('${'):
                        # 입력이 다른 노드의 출력을 참조하는 경우
                        referenced_node = input_value.split('.')[0].replace('${', '')
                        dot.edge(referenced_node, node_name)

    # 그래프 저장
    dot.render(current_dir+'/flow_visualization', format='png', cleanup=True)
    print("Flow visualization saved as 'flow_visualization.png'")

# 스크립트 실행
visualize_flow(current_dir+'/flow.dag.yaml')