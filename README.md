1. Acessar a Console do AWS IoT
   1.1 Vídeo de ajuda: https://youtu.be/lKupMQzEUN8
   1.2 Fonte para consulta: https://aws.amazon.com/pt/blogs/aws-brasil/comecando-com-o-aws-iot-parte-1/

3. Criar uma Coisa,  Criar um Certificado, Criar uma Política, Vincular o Dispositivo, Política e Certificado
   2.1 Vídeo de ajuda: em breve
   3.2 Fonte para consulta: https://aws.amazon.com/pt/blogs/aws-brasil/comecando-com-o-aws-iot-parte-1/

4. Preparar o Ambiente para Simular um Dispositivo
   4.1 Vídeo de ajuda: em breve
   4.2 Crie seu repositorio no git hub com seu kit de conexão.
   4.3 Baixo o arquivo "coisa.py" e realize o upload no seu repositorio.
   4.4 Criar uma instancia no AWS:
     4.4.1 Vídeo de ajuda: https://youtu.be/drhDR7AZ-0E
   4.4 Executar os comandos no console da Instancia:
    sudo yum install git
    sudo yum install pip
    sudo yum remove awscli
    sudo curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    sudo unzip awscliv2.zip
    sudo ./aws/install
    mkdir -p ~/tutorial/iot_parte_1
    cd ~/tutorial/iot_parte_1
    git clone https://github.com/<<seurepositoriogithub>>.git 
    cd MeuPrimeiroDispositivoIoT
    chmod +x start.sh
    wget https://www.symantec.com/content/en/us/enterprise/verisign/roots/VeriSign-Class%203-Public-Primary-Certification-Authority-G5.pem -O /home/ec2-user/tutorial/iot_parte_1/rootCA.pem
   4.5 Fonte para consulta: https://aws.amazon.com/pt/blogs/aws-brasil/comecando-com-o-aws-iot-parte-1/

6. Executando o Programa com kit de conexão
   5.1 Vídeo de ajuda: em breve
   5.2 Execute no prompt da instancia
   ./start.sh
   5.3 Fonte para consulta: https://aws.amazon.com/pt/blogs/aws-brasil/comecando-com-o-aws-iot-parte-1/
   5.2 Fonte para consulta: https://aws.amazon.com/pt/blogs/aws-brasil/comecando-com-o-aws-iot-parte-1/

7. Obtendo o seu Endpoint para Conexão com o AWS IoT
  6.1 Vídeo de ajuda: em breve
  6.2 Fonte para consulta: https://aws.amazon.com/pt/blogs/aws-brasil/comecando-com-o-aws-iot-parte-1/

8. Validando o funcionamento
  7.1 Vídeo de ajuda: em breve
  7.2 Inscrever nos tópicos:
    sdk/test/python
    dispositivos/MeuPrimeiroDispositivo/reportar
  7.3 Fonte para consulta: https://aws.amazon.com/pt/blogs/aws-brasil/comecando-com-o-aws-iot-parte-1/
   
OBS: Para encerrar o programa pressione CTRL+C no console da instancia.
