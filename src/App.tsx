import React, { useState } from 'react';
import { ref, push } from 'firebase/database';
import { database } from './firebase';
import { Bus, User, CheckCircle2, AlertCircle } from 'lucide-react';

interface FormData {
  nome: string;
  idade: number;
  rg: string;
  celular: string;
  organizacao: string;
}

const initialFormData: FormData = {
  nome: '',
  idade: 18,
  rg: '',
  celular: '',
  organizacao: 'Quórum de Élderes'
};

function App() {
  const [formData, setFormData] = useState<FormData>(initialFormData);
  const [status, setStatus] = useState<{ type: 'success' | 'error' | null; message: string }>({
    type: null,
    message: ''
  });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!formData.nome || !formData.idade || !formData.rg || !formData.celular) {
      setStatus({
        type: 'error',
        message: 'Por favor, preencha todos os campos obrigatórios.'
      });
      return;
    }

    try {
      const caravanaRef = ref(database, 'Caravana');
      await push(caravanaRef, formData);
      setStatus({
        type: 'success',
        message: 'Cadastro realizado com sucesso!'
      });
      setFormData(initialFormData);
    } catch (error) {
      setStatus({
        type: 'error',
        message: 'Erro ao realizar o cadastro. Tente novamente.'
      });
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-50 to-white">
      <div className="max-w-4xl mx-auto px-4 py-12">
        <div className="text-center mb-12">
          <div className="flex items-center justify-center gap-3 mb-4">
            <Bus className="w-12 h-12 text-blue-600" />
            <h1 className="text-4xl font-bold text-gray-800">
              Cadastro para Caravana
            </h1>
          </div>
          <p className="text-gray-600 text-lg">
            Templo de Campinas
          </p>
        </div>

        <div className="bg-white rounded-lg shadow-xl p-8">
          <div className="flex items-center gap-2 mb-6">
            <User className="w-6 h-6 text-blue-600" />
            <h2 className="text-2xl font-semibold text-gray-700">
              Dados do Participante
            </h2>
          </div>

          <form onSubmit={handleSubmit} className="space-y-6">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Nome Completo
                </label>
                <input
                  type="text"
                  value={formData.nome}
                  onChange={(e) => setFormData({ ...formData, nome: e.target.value })}
                  className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  maxLength={50}
                  required
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Idade
                </label>
                <input
                  type="number"
                  value={formData.idade}
                  onChange={(e) => setFormData({ ...formData, idade: parseInt(e.target.value) })}
                  className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  min={1}
                  max={120}
                  required
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  RG
                </label>
                <input
                  type="text"
                  value={formData.rg}
                  onChange={(e) => setFormData({ ...formData, rg: e.target.value })}
                  className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  maxLength={20}
                  required
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  Celular
                </label>
                <input
                  type="tel"
                  value={formData.celular}
                  onChange={(e) => setFormData({ ...formData, celular: e.target.value })}
                  className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  maxLength={15}
                  required
                />
              </div>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-3">
                Organização
              </label>
              <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4">
                {[
                  'Quórum de Élderes',
                  'Sociedade de Socorro',
                  'Moças',
                  'Rapazes',
                  'Primária'
                ].map((org) => (
                  <label
                    key={org}
                    className={`
                      flex items-center justify-center p-3 border rounded-md cursor-pointer
                      ${formData.organizacao === org
                        ? 'bg-blue-50 border-blue-500 text-blue-700'
                        : 'border-gray-300 text-gray-700 hover:bg-gray-50'}
                    `}
                  >
                    <input
                      type="radio"
                      name="organizacao"
                      value={org}
                      checked={formData.organizacao === org}
                      onChange={(e) => setFormData({ ...formData, organizacao: e.target.value })}
                      className="sr-only"
                    />
                    <span className="text-sm font-medium">{org}</span>
                  </label>
                ))}
              </div>
            </div>

            {status.type && (
              <div className={`p-4 rounded-md ${
                status.type === 'success' ? 'bg-green-50' : 'bg-red-50'
              }`}>
                <div className="flex items-center gap-2">
                  {status.type === 'success' ? (
                    <CheckCircle2 className="w-5 h-5 text-green-500" />
                  ) : (
                    <AlertCircle className="w-5 h-5 text-red-500" />
                  )}
                  <span className={status.type === 'success' ? 'text-green-700' : 'text-red-700'}>
                    {status.message}
                  </span>
                </div>
              </div>
            )}

            <button
              type="submit"
              className="w-full bg-blue-600 text-white py-3 px-6 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-colors"
            >
              Cadastrar
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default App;