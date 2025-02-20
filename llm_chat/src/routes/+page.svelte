<script>

	export let data;

	const API = "http://localhost:8000";

	// 入力するテキスト
	let inputText = "";

	// API から返ってきた返答
	let response = data.data;

	// API から返ってきた音声ファイルの URL
	let audioUrl = "";

	// エラー状態を管理するための変数(必要に応じて)
	let errorMessage = "";

	// 読み込み待ちステータス
	let isLoading = false;

	// API に POST してデータを受け取り、画面に反映する
	async function handleSubmit() {
		isLoading = true;
		errorMessage = "";
		try {
			const requestBody = {
				text: inputText
			};
			inputText = "";

			// fetch で API に POST
			const res = await fetch(`${API}/post`, {
				method: "POST",
				headers: {
					"Content-Type": "application/json"
				},
				body: JSON.stringify(requestBody)
			});

			// 応答を JSON としてパース
			if (!res.ok) {
				// エラー時の処理(レスポンスが 2xx でない場合)
				throw new Error(`API Error: ${res.status} ${res.statusText}`);
			}
			const data = await res.json();
			response = Array.isArray(data.messages) ? data.messages : [];
			audioUrl = `${API}/${data.audio_path}`;
			// エラーのリセット
			errorMessage = "";
		} catch (err) {
			errorMessage = err.message;
		} finally {
			isLoading = false;
		}
	}

	// 会話履歴を削除
	async function resetHistory(e) {
		const originalLabel = e.target.innerHTML;
		const agreement = confirm("履歴をリセットします");
		if (agreement) {
			const resetBody = {
				agreement: true
			};
			try {
				const res = await fetch(`${API}/reset`, {
					method: "POST",
					headers: {
						"Content-Type": "application/json"
					},
					body: JSON.stringify(resetBody)
				});
				if (!res.ok) {
					alert(`削除できませんでした。（${res.status} ${res.statusText}）`);
					throw new Error(`API Error: ${res.status} ${res.statusText}`);
				}
				// const result = await res.text();
				const chatArea = document.getElementById("chat");
				if (chatArea) {
					// chatArea.innerHTML = "";
					response = [];
				}
				e.target.innerHTML = "削除しました!";
				window.setTimeout(() => {
					e.target.innerHTML = originalLabel;
				}, 1000);
			} catch (err) {
				errorMessage = err.message;
			}
		} else {
			return
		}
	}
	function handleKeydown(event) {
		// Mac Command + Enter または Enter 単独で送信
		if (
			(event.metaKey && event.key === 'Enter')
		) {
			event.preventDefault();
			handleSubmit();
		}
	}
</script>

<div class="container mx-auto max-w-screen-md">
	<div class="h-dvh w-full p-4">
		<div id="chat" class="flex flex-col">
			{#each response as res}
			<div class={`rounded-md p-4 mt-4 w-4/5 text-black
			${res.role === "assistant" ?
				"bg-green-100 self-end border border-green-400" :
				"bg-gray-200"}`}>
				{res.content}
			</div>
			{/each}
		</div>

		<textarea
			name=""
			id=""
			class="mt-5 h-32 w-full rounded-md border border-gray-300 bg-gray-50 p-2.5 text-gray-900 focus:border-blue-500 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400 dark:focus:border-blue-500 dark:focus:ring-blue-500"
			bind:value={inputText}
			on:keydown={handleKeydown}
		></textarea>
		<div class="flex justify-between">
			<button
				type="submit"
				class="mt-2 rounded-md px-4 py-2
				border border-gray-400 bg-gradient-to-b from-gray-500 to-gray-700 p-2 text-white
				hover:from-gray-300 hover:to-gray-500
				active:from-gray-700 active:to-gray-900
				disabled:from-gray-900 disabled:to-gray-900"
				on:click={handleSubmit}
				disabled={isLoading}
			>{#if isLoading}返答を待っています{:else}送信する{/if}
			</button>
	
			<button
				type="submit"
				class="mt-2 rounded-md px-4 py-2
				border border-red-400 bg-red-800 text-white"
				on:click={resetHistory}
				disabled={isLoading}
			>履歴を削除する</button>
		</div>
		<div id="voice" class="mt-10">
			{#if audioUrl}
			<audio
				src={audioUrl}
				controls
				autoplay
			></audio>
			{/if}
		</div>
	</div>
</div>
