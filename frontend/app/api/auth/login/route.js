const { NextResponse } = require("next/server");
const axios = require("axios").default;

export async function POST(request) {
  const body = await request.json();
  const { username, password } = body;

  if (!username || !password) {
    return NextResponse.json(
      { error: "Missing username or password" },
      { status: 400 }
    );
  }

  try {
    const response = await axios.post(
      `${process.env.BACKEND_URL}/api/auth/jwt/create/`,
      { username, password },
      {
        headers: {
          "Content-Type": "application/json",
          "User-Agent": "insomnia/9.3.2",
        },
      }
    );

    console.log("Login response:");
    console.log(response.data);

    return NextResponse.json(response.data, { status: 200 });
  } catch (error) {
    return NextResponse.json({ error }, { status: 400 });
  }
}
