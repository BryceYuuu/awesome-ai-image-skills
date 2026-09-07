# Deploy to GitHub Pages

## Fastest way

1. Upload the whole `awesome-ai-image-skills` folder to a GitHub repository.
2. Make sure `index.html` is in the repository root.
3. Go to **Settings → Pages**.
4. Under **Build and deployment**, choose:
   - **Source**: Deploy from a branch
   - **Branch**: `main`
   - **Folder**: `/ (root)`
5. Save.
6. Wait 1–3 minutes. Your site will appear at:
   - `https://<your-github-username>.github.io/<repo-name>/`

## Notes

- This project already includes a root `index.html`, so GitHub Pages can serve it directly.
- `.nojekyll` is included to avoid GitHub Pages filtering files unexpectedly.
- `preview.html` is kept as a working copy; `index.html` is the GitHub Pages entry file.

## Recommended repository metadata

- Repository name: `awesome-ai-image-skills`
- Description: `Curated high-aesthetic AI image skills for photo editing, zine posters, editorial design, social covers & visual workflows — with examples, sources and copy-ready prompts.`
- Homepage after Pages: `https://bryceyuuu.github.io/awesome-ai-image-skills/`
- Topics: see [`REPO_METADATA.md`](REPO_METADATA.md)
