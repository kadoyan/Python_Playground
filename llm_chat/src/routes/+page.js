export async function load({fetch}) {
	const API = 'http://localhost:8000/history';
	const res = await fetch(API);
	const data = await res.json();

	// ページに渡したいデータを return
	return {
		data
	};
}
