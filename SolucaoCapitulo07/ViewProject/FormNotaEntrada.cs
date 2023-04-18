using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using ControllerProject;
using ModelProject;

namespace ViewProject
{
    public partial class FormNotaEntrada : Form
    {
        private NotaEntradaController controller;
        private FornecedorController fornecedorController;
        private ProdutoController produtoController;
        private NotaEntrada notaAtual;
        public FormNotaEntrada(NotaEntradaController controller,FornecedorController fornecedorController, ProdutoController produtoController)
        {
            InitializeComponent();
            this.controller = controller;
            this.fornecedorController =
            fornecedorController;
            this.produtoController = produtoController;
            InicializaComboBoxs();
        }
    }
}
