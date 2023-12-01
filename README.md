# Desafio IA
# Guilherme Mariano

## Primeira Parte

### No arquivo tracker runner temos a resolução do desafio que consistiu em identificar pessoas que estão passando por uma praça e assinalar uma id e uma "bounding box" para cada
### A contagem de pessoas que estão passando pela cena é feita através da identificação do número total de 'ids' diferentes
### O objeto Tracker tem como parâmetros opcionais o endereço do video a ser estudado e o modelo do YOLO que o usuário deseja utlizar.

## Segunda Parte
### No arquivo FaceBlurRunner temos a solução para o desafio de identificar rostos e aplicar blurring.
### O caminho do video é um parâmetro opcional. Os rostos são identificados usando um modelo pré treinado do opencv2.
### Para aplicar o efeito de blurring é necessário pressionar a tecla 'b'. O blurring pode ser ligado e desligado por meio desse input.
### A ideia inicial seria usar as bounding boxes do YOLOV8 para extrair fragmentos do frame com imagens individuais de pessoas.
### E então seria aplicado a identificação facial do OpenCV2. Visto que o YOLOv8 não tem solução nativa para identificação de rostos.
