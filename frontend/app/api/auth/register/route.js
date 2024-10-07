// api/auth/register/route.js
const { NextResponse } = require("next/server");
const axios = require("axios").default;

export async function POST(request) {
  const body = await request.json();
  const { first_name, last_name, username, email, password, re_password } =
    body;

  if (
    !first_name ||
    !last_name ||
    !username ||
    !email ||
    !password ||
    !re_password
  ) {
    return NextResponse.json(
      { error: "Missing required values" },
      { status: 400 }
    );
  }

  try {
    const response = await axios.post(
      `${process.env.BACKEND_URL}/api/auth/users/`,
      { first_name, last_name, username, email, password, re_password },
      {
        headers: {
          "Content-Type": "application/json",
          "User-Agent": "insomnia/9.3.2",
        },
      }
    );

    console.log("Register response:");
    console.log(response.data);

    return NextResponse.json(response.data, { status: 200 });
  } catch (error) {
    console.error(error);
    return NextResponse.json({ error }, { status: 400 });
  }
}
