-- 30/10/2026 — Annonce du hub pour l'article Actus « Leçon 2 de la chouette : les 15 ouvertures »
-- À utiliser SEULEMENT si l'annonce n'a pas été créée par la case « 📣 Annoncer aussi sur le hub »
-- en enregistrant l'article dans l'admin 📰 Actus (elle est cochée par défaut).
-- À passer dans phpMyAdmin (base chouette), onglet SQL, APRÈS article_lecon2.sql.
-- Annonce « 📰 Article Actus » (image, titre et chapô repris de l'article), popup + bandeau,
-- visible du dimanche 8/11/2026 10:30 au samedi 21/11/2026 23:59 (heure de Paris).
UPDATE announcements SET sort_order = sort_order + 1
WHERE NOT EXISTS (SELECT 1 FROM (SELECT a.id FROM announcements a JOIN news_articles n ON n.id = a.news_id
                                 WHERE a.kind = 'article' AND n.slug = 'lecon-2-ouvertures') x);

INSERT INTO announcements (kind, title_fr, news_id, color, show_popup, show_banner, audience, starts_at, ends_at, is_active, sort_order)
SELECT 'article', '', n.id, '#c9954a', 1, 1, 'all', '2026-11-08 10:30:00', '2026-11-21 23:59:00', 1, 0
FROM news_articles n
WHERE n.slug = 'lecon-2-ouvertures'
  AND NOT EXISTS (SELECT 1 FROM announcements a WHERE a.kind = 'article' AND a.news_id = n.id);

-- Vérification : 1 ligne, du 2026-11-08 10:30 au 2026-11-21 23:59, is_active = 1
SELECT a.id, a.kind, a.news_id, a.starts_at, a.ends_at, a.is_active
FROM announcements a JOIN news_articles n ON n.id = a.news_id WHERE n.slug = 'lecon-2-ouvertures';
