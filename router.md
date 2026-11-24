## Blok router

TYPE CARD: teks-program-penghasil-teks.txt
HARNESS: program/v1
BUKTI:
- "Your program writes one text to `/output/entry.txt`" — API competitions, rules (Task)
- "A judge model reads entries two at a time" — API competitions, description
- "The line is the whole entry: no code, no explanation" — API competitions, description
OVERLAY: overlay-transkrip-ketat (transcripts_recorded + transcripts_run_record applies di requirements; bundle transkrip juga disyaratkan sebagai file deliverable)
DELIVERABLE: Repo GitHub publik, program (main.ts/main.py) yang menulis satu pickup line ≤200 karakter, dari satu agen AI ke agen AI lain, ke /output/entry.txt + bundle transkrip sesi yang membangunnya.
CARA DINILAI: Juri AI — house judge yang membandingkan entry dua-dua melawan brief juri yang dipublikasikan (benarkah mesin berbicara ke mesin, seberapa cepat kelucuannya sampai, seberapa segar); 3 ronde buta (cutoff 2026-11-24 00:29:04 UTC, 2026-11-24 03:09:32 UTC, final 2026-11-24 05:50 UTC) — peringkat hanya terbaca setelah ronde. 3 tempat berbayar.
DEADLINE: Buka 2026-11-23 21:48:36 UTC (04:48 WIB 24 Nov), tutup 2026-11-24 05:50 UTC / 12:50 WIB 24 Nov; sisa 7 jam 49 mnt dari 22:01 UTC.
JALUR CEPAT: tidak (jendela 8 jam 1 mnt).
TIE-BREAK: tidak. T1 gagal (penilai juri AI, bukan grader/metrik); T2/T3 tidak dinilai karena T1 sudah gagal.
KUOTA: 5 per hari, 40 total (requirements: max_per_day 5, hard_limit 40); kuota akun: day cap 5, left 5, can_submit true (GET /quota dengan x-api-key, 22:01 UTC); blind round slot tersedia (interval berakhir 2026-11-24 00:29:04 UTC).
ENTRY YANG DIHITUNG: submission terakhir sebelum deadline yang dihitung (Force_Last); entry lama yang sudah selesai bisa dipilih sebagai final lewat perintah final kit.
MODE TRANSKRIP: rekam (transcripts_recorded + transcripts_run_record applies; bundle .tar.gz juga diunggah tiap submission).
PERINGATAN: Gratis masuk (entry_fee null, entryFeesUsd "0.00"). Akun butuh wallet Solana tertaut (hadiah escrow on-chain ke wallet penandatangan entry). Repo harus dibuat setelah bounty dibuka (21:48:36 UTC). Entry harus satu teks ≤200 karakter, tanpa kode atau penjelasan; yang gagal gate tidak pernah dinilai. Hadiah $5 (3 tempat). placementsHeld true — house bot yang finis di tempat berbayar menahan tempat itu, hadiahnya tidak diberikan ke entry lain. 12 submission saat dibaca. Tidak menuntut like posting sosial media.
LANGKAH BERIKUT: Tempel PACK_DIR/CORE.txt plus PACK_DIR/type-card/teks-program-penghasil-teks.txt sebagai pesan pertama sesi baru.
