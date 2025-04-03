import eslint from '@eslint/js';

export default [
	{
		ignores: ['node_modules/'],
	},
	eslint.configs.recommended,
	{
		languageOptions: {
			ecmaVersion: 2020,
			sourceType: 'module',
			globals: {
				console: 'readonly', // Définit 'console' comme une variable globale en lecture seule
			},
		},
		rules: {
			'no-unused-vars': 'warn',
			'no-console': 'off', // Désactive la règle qui interdit l'utilisation de console
		},
	},
];
