import { descopeClient } from "../utils/consts";

export const authMiddleware = async (req, res, next) => {
  try {
    const authorizationHeader = req.headers.authorization || "";

    const sessionToken = authorizationHeader.split("Bearer ")[1] || "";

    req.authInfo = await descopeClient.validateSession(sessionToken);
    next();
  } catch (e) {
    console.error(e);
    res.status(401).json({ error: "Unauthorized." });
  }
};
