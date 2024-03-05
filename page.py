import cherrypy
from classes.cadastro import *

class PaginaCadastro():
    topo = open("html/cabecalho.html", encoding="utf-8").read()
    rodape = open("html/menu.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        return self.montaFormulario()

    def montaFormulario(self, pId=0, pNome='', pGenero='', pFoto='', pArt='', pLink=''):
        html = self.topo
        html += '''
             <form name="FormCadastro" action="gravarCadastro" method="post" "enctype="/file">
                <div class="separar">
                    <input type="hidden" id="txtId" name="txtId" value="%s"/>
        		</div>
                <div class="separar">
                    <label for="txtfoto">Foto:</label>
                    <input type="file" id="txtfoto" name="txtfoto" class="branco" value="%s" required="required" >
                </div>
                <div class="separar">
                    <label for="nomeArt">Nome Artistico: </label>
                    <input type="text" name="txtart" id="txtart" class="preto" size="20" value="%s" required="required" placeholder="Nome artistico/banda" >
                </div>

                <div class="separar">
                    <label for="nome">Nome: </label>
                    <input type="text" name="txtnome" id="txtnome" class="preto" size="20" value="%s" required="required" placeholder="Digite um nome" >
                </div>

                <div class="separar">
                    <label for="genero">Gênero musical: </label>
                    <input type="text" name="txtgenero" id="txtgenero" class="preto" size="20" value="%s" required="required" placeholder="Digite um gênero musical" >
                </div>

                <div class="separar">
                    <label for="link">Link: </label>
                    <input type="url" name="txtlink" id="txtlink" class="preto" size="20" value="%s" required="required" placeholder="Digite um link" >
                </div>

                <div class="separar">
                    <input type="submit" name="btnGravar" id="btnGravar"  class="preto" value="cadastrar">
                </div>
            </form>
            ''' % (pId, pFoto, pArt, pNome,  pGenero,   pLink)
        html += self.montaTabela()
        html += self.rodape
        return html

    def montaTabela(self):
        html = '''<table class="alinha" style="margin: 0 auto; text-color: black;" border="1">
    <tr>
        <th> ID </th>
        <th> Nome </th>
        <th> Genero </th>
        <th> Foto </th>
        <th> Nome Artistico </th>
        <th> Site </th>
        <th> Ações </th>
    </tr>'''
        objCadastro = cadastro() # criando um objeto do tipo Especie
        dados = objCadastro.obterCadastros() # lista com os dados  do SQL
        for cad in dados:
            html += '''<tr>
                         <td> %s </td>
                         <td> %s </td>
                         <td> %s </td>
                         <td> %s </td>
                         <td> %s </td>
                         <td> %s </td>
                         <td style="text-align:center">
                          <a href="alterarCadastro?idtab=%s">[Alterar]</a>
                          </br>
                          <a href="excluirCadastro?idtab=%s">[Excluir]</a>  
                         </td>
                       </tr> ''' % (cad["id"],cad["nome"],cad["genero"], cad["foto"], cad["art"], cad["link"],cad["id"],cad["id"])

        html += '</table> <br/> <br/>'
        return html

    @cherrypy.expose()
    def gravarCadastro(self,txtId,txtnome,txtgenero, txtfoto, txtart, txtlink, btnGravar):
        if len(txtnome)>0:
            objCadastro = cadastro()
            objCadastro.set_nome(txtnome)
            objCadastro.set_genero(txtgenero)
            objCadastro.set_foto(txtfoto)
            objCadastro.set_art(txtart)
            objCadastro.set_link(txtlink)
            retorno = 0 # variável para controlar o sucesso!!
            if int(txtId) == 0: # novo registro no banco
                retorno = objCadastro.gravar()
            else: # gravar a alteração de um registro
                # neste caso da alteração a gente precisa carregar o id no objeto, quanto é uma nova espécie não precisa porque o id é gerado de forma automática
                objCadastro.set_id(int(txtId))
                retorno = objCadastro.alterar()
            if retorno > 0:
                return '''
                    <script>
                       alert("O cadastro %s foi gravada com sucesso!!");
                       window.location.href = "/cadastro"
                    </script>
                ''' % (txtnome)
            else:
                return '''
                   <h2>Erro ao gravar cadastro <b>%s</b>. </h2>
                   <a href="/">voltar</a> 
                ''' % (txtnome)
        else: #if len(txtDescr)>0:
            return '''
               <h2>O nome deve ser informada.</h2>
               <a href="/">voltar</a> 
            '''

    @cherrypy.expose()
    def excluirCadastro(self,idtab):
        objCadastro = cadastro()
        objCadastro.set_id(int(idtab))
        if objCadastro.excluir() > 0:
            raise cherrypy.HTTPRedirect('/cadastro')
        else:
            return '''
            <h2> Não foi possível excluir o cadastro!!</h2>
            [<a href="/">Voltar</a>]
            '''

    @cherrypy.expose()
    def alterarCadastro(self, idtab):
        objCadastro = cadastro()
        # estamos buscando o objeto com os dados que foram passados por parâmetro neste método
        dadosCadastroSelec = objCadastro.obterCadastro(idtab)
        # chamando o método para montar o formulário com os valores do banco de dados nos campos do formulário
        return self.montaFormulario(dadosCadastroSelec[0]['id'], dadosCadastroSelec[0]['nome'], dadosCadastroSelec[0]['genero'], dadosCadastroSelec[0]['foto'], dadosCadastroSelec[0]['art'], dadosCadastroSelec[0]['link'])