# Selos da frente do cobre

A árvore carrega **um** par: `AUDITORIA_SOL_COBRE_MANIFEST_R1_<alvo>.json` e
`AUDITORIA_SOL_COBRE_HASHES_RESPONSE_R1_<alvo>.json`, para o alvo vigente.
Os pares anteriores foram retirados da árvore e continuam no git — o commit de cada
um está na tabela. `git show <commit>:<arquivo>` recupera o byte, e o sha256 abaixo
confere se o que veio é o mesmo.

| alvo_commit | sha256 do manifesto | sha256 da resposta | data | commit do par |
|---|---|---|---|---|
| `3fd33c3b` | `a7ad27d7d0115450…` | `c5629e1d6efd038f…` | 2026-11-25T16:02:57Z | `7d2db6d28b76` |
| `b6c882f7` | `72f2a0d41ca34721…` | `a0983e90f38ae905…` | 2026-11-25T16:01:51Z | `91dc854310f3` |
| `ad00bf6b` | `7f14de72e787b13c…` | `40c4b63e12dd8926…` | 2026-11-25T13:37:08Z | `25d97434db77` |
| `ae3ba67a` | `22b26dcc8db0e5ba…` | `30aa369e84b006e7…` | 2026-11-25T13:35:23Z | `89b83f5f4fef` |
| `e617edbc` | `1020ded3a957e0da…` | `c899d543edb1a6f3…` | 2026-11-25T13:31:01Z | `8654dd3e47f1` |
| `8b49a604` | `133eace293f4358b…` | `cf49c010a6f39485…` | 2026-11-25T13:24:16Z | `6598247aff60` |
| `54f89240` | `f0dbc03bd6a2b670…` | `ef757da61760648b…` | 2026-11-25T13:16:32Z | `73b89b04a68a` |
| `436b9fd0` | `848f32b21e9cec76…` | `6930cd870202f126…` | 2026-11-25T13:13:09Z | `e36056753014` |
| `1e59afc7` | `09b498a80e21a3b6…` | `b21582c6384f8dee…` | 2026-11-25T13:09:29Z | `50b4088eef47` |
| `72205a25` | `fb9c0a42e7960192…` | `0cc6805d3036ea72…` | 2026-11-25T13:05:56Z | `12935100df96` |
| `1a4c858d` | `a2448f0f3d69c71f…` | `96b5b06c2edc48ad…` | 2026-11-25T13:01:37Z | `7362e7b32524` |
| `729c4deb` | `d98a2235a8afa830…` | `d305cfbf5858199a…` | 2026-11-25T12:57:14Z | `517bc7e0b5fe` |
| `ec47267d` | `abafbb0861003e2f…` | `1c9f662d159fe5a7…` | 2026-11-25T12:53:08Z | `8918e52c95de` |
| `b6fe7936` | `b349322702de5e87…` | `1d429df66517841b…` | 2026-11-25T12:45:32Z | `0bdaea9f4b3a` |
| `7e2252b5` | `fb5a0a1b027f8077…` | `93b006de4b5639d3…` | 2026-11-25T12:39:19Z | `de4cbd884317` |
| `f7b2da8e` | `a39211b6b2746bfc…` | `b73085628874048d…` | 2026-11-25T12:22:39Z | `355bc5dd0777` |
| `d2f46fc8` | `27e343391bca1aa4…` | `a22322b360c69c47…` | 2026-11-25T12:02:31Z | `0658d02ea79e` |
| `26b935df` | `1c7fb70154d6ef0f…` | `78680c5843c5bd14…` | 2026-11-25T11:04:29Z | `5bf1eeb1ba5e` |
| `b0f3f82b` | `465003987fcea430…` | `11ebd892c799846e…` | 2026-11-25T10:58:41Z | `fc137e5c0272` |

Total de selos indexados: **19**.

Gerado por `scripts/gerar_selos_cobre.py` a partir do histórico; não editar à mão.
