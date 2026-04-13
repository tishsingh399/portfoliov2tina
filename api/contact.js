export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { name, email, message, botcheck } = req.body;

  // Silently drop bot submissions
  if (botcheck) {
    return res.status(200).json({ success: true });
  }

  // Basic validation
  if (!name || !email || !message) {
    return res.status(400).json({ error: 'Missing required fields' });
  }

  const key = process.env.WEB3FORMS_ACCESS_KEY;
  if (!key) {
    return res.status(500).json({ error: 'Server configuration error' });
  }

  const response = await fetch('https://api.web3forms.com/submit', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      access_key: key,
      name,
      email,
      message,
      subject: `Portfolio Inquiry from ${name} — tinasingh.app`,
      from_name: 'tinasingh.app Contact Form'
    })
  });

  const data = await response.json();
  return res.status(response.status).json(data);
}
