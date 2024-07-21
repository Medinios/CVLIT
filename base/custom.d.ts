declare global {
  namespace NodeJS {
    interface ProcessEnv {
      PORT: number;
      AUTH0_SECRET: string;
      AUTH0_ISSUER_BASE_URL: string;
      AUTH0_CLIENT_ID: string;
      AUTH0_API_IDENTIFIER: string;
      AUTH0_BACKEND_BASE_URL: string;
      LINKEDIN_URL: string;
      LINKEDIN_CLIENT_ID: string;
      LINKEDIN_CLIENT_SECRET: string;
      BACKEND_LINKEDIN_REDIRECT_URI: string;
      TIKTOK_CLIENT_KEY: string;
      TIKTOK_CLIENT_SECRET: string;
      TIKTOK_APP_ID: string;
      FRONTEND_BASE_URL: string;
      DB_CONNECTION_STRING: string;
      DB_USERNAME: string;
      DB_PASSWORD: string;
      DB_HOST: string;
      ENCRYPTION_SECRET: string;
    }
  }
}

export {};
