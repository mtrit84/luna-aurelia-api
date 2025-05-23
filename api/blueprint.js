export default function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method not allowed" });
  }

  const { business_type, target_audience, language } = req.body;

  if (!business_type) {
    return res.status(400).json({ error: "Missing required field: business_type" });
  }

  const message = `🔧 Luna Aurelia hat den Blueprint für "${business_type}" erstellt – Sprache: ${language || "nicht angegeben"}, Zielgruppe: ${target_audience || "nicht angegeben"}.`;

  return res.status(200).json({
    success: true,
    message,
    instructions: [
      "1. Inhalte generieren",
      "2. Website bauen",
      "3. Plugin aktivieren"
    ]
  });
}