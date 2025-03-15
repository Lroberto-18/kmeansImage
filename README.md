# kmeansImage

Gostaria de compartilhar um exemplo prático de como o algoritmo K-means pode ser aplicado para resolver
problemas de segmentação de imagens e compressão de dados.
Este projeto foi inspirado no livro "Pattern Recognition and Machine Learning" de Christopher M. Bishop".

A segmentação de imagens é o processo de dividir uma imagem 
em regiões que possuem características visuais semelhantes, 
como cor ou textura. Cada pixel de uma imagem é representado como um ponto em 
um espaço tridimensional (R, G, B), onde cada dimensão corresponde à intensidade das cores vermelha, verde e azul.
O algoritmo K-means agrupa esses pixels em K clusters, onde cada cluster é representado por uma cor média (centroide).

Além da segmentação, o K-means também pode ser usado para compressão de imagens. 
Em vez de armazenar todos os pixels originais, armazenamos apenas os rótulos dos clusters e os centroides.
Isso reduz significativamente a quantidade de dados necessários para representar a imagem, 
embora com alguma perda de qualidade (compressão com perdas).

Métricas de Qualidade e Compressão
Para avaliar a qualidade da imagem comprimida e o nível de compressão:

PSNR (Peak Signal-to-Noise Ratio) - Medido em dB.

MSE é o erro quadrático médio entre a imagem original e a comprimida.

E a Taxa de Compressão - Medido em x:

A taxa de compressão indica quantas vezes a imagem foi comprimida. Quanto maior a taxa, maior a compressão.
