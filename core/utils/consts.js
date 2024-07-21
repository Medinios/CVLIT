import DescopeClient from "@descope/node-sdk";

export const descopeClient = DescopeClient({
  projectId: process.env.PROJECT_ID,
});
