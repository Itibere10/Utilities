# SELECIONANDO O DIRETÓRIO
USER_DIR='C:\Users\itibe'
CODE='ed25519'
MAIL='itibere.filho@gmail.com'

# CONFIGURANDO O SSH
cd $USER_DIR
echo '> Gerando ssh...'
ssh-keygen -t $CODE -C "$MAIL"
cd .ssh/
echo '> Chave SSH para inserir no github:'
cat id_$CODE.pub
