import { useState, useEffect } from 'react';
import apiClient from '@/lib/apiClient';

interface User {
  id: string;
  email: string;
  full_name?: string;
  avatar_url?: string;
  email_confirmed: boolean;
  created_at: string;
}

interface AuthTokens {
  access: string;
  refresh: string;
}

interface AuthResponse {
  user: User;
  tokens: AuthTokens;
}

export const useAuth = () => {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Check if user is already logged in
    const checkAuth = async () => {
      const token = localStorage.getItem('access_token');

      if (token) {
        try {
          const response = await apiClient.get('/auth/me/');
          setUser(response.data);
        } catch (error) {
          console.error('Auth check failed:', error);
          localStorage.removeItem('access_token');
          localStorage.removeItem('refresh_token');
          setUser(null);
        }
      }

      setLoading(false);
    };

    checkAuth();
  }, []);

  const signUp = async (email: string, password: string, fullName?: string) => {
    try {
      const response = await apiClient.post<AuthResponse>('/auth/register/', {
        email,
        password,
        password_confirm: password,
        full_name: fullName || '',
      });

      const { user, tokens } = response.data;

      // Store tokens
      localStorage.setItem('access_token', tokens.access);
      localStorage.setItem('refresh_token', tokens.refresh);

      setUser(user);

      return { error: null };
    } catch (error: any) {
      return {
        error: {
          message: error.response?.data?.email?.[0] || error.response?.data?.password?.[0] || 'Registration failed'
        }
      };
    }
  };

  const signIn = async (email: string, password: string) => {
    try {
      const response = await apiClient.post<AuthResponse>('/auth/login/', {
        email,
        password,
      });

      const { user, tokens } = response.data;

      // Store tokens
      localStorage.setItem('access_token', tokens.access);
      localStorage.setItem('refresh_token', tokens.refresh);

      setUser(user);

      return { error: null };
    } catch (error: any) {
      return {
        error: {
          message: error.response?.data?.error || 'Login failed'
        }
      };
    }
  };

  const signInWithGoogle = async () => {
    try {
      // This will open Google OAuth in a popup
      // You'll need to implement the OAuth flow with Google
      // For now, return a placeholder
      return {
        error: {
          message: 'Google OAuth requires additional setup. Please use the Google Sign-In button with proper OAuth flow.'
        }
      };
    } catch (error: any) {
      return {
        error: {
          message: error.response?.data?.error || 'Google sign-in failed'
        }
      };
    }
  };

  const signInWithFacebook = async () => {
    try {
      // This will open Facebook OAuth in a popup
      // You'll need to implement the OAuth flow with Facebook
      return {
        error: {
          message: 'Facebook OAuth requires additional setup and credentials.'
        }
      };
    } catch (error: any) {
      return {
        error: {
          message: error.response?.data?.error || 'Facebook sign-in failed'
        }
      };
    }
  };

  const signInWithApple = async () => {
    try {
      // This will open Apple OAuth in a popup
      // You'll need to implement the OAuth flow with Apple
      return {
        error: {
          message: 'Apple OAuth requires additional setup and credentials.'
        }
      };
    } catch (error: any) {
      return {
        error: {
          message: error.response?.data?.error || 'Apple sign-in failed'
        }
      };
    }
  };

  const signOut = async () => {
    try {
      const refreshToken = localStorage.getItem('refresh_token');

      if (refreshToken) {
        await apiClient.post('/auth/logout/', {
          refresh_token: refreshToken,
        });
      }

      // Clear tokens and user state
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
      setUser(null);

      return { error: null };
    } catch (error: any) {
      // Even if logout fails on server, clear local state
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
      setUser(null);

      return {
        error: {
          message: error.response?.data?.error || 'Logout failed'
        }
      };
    }
  };

  const resetPassword = async (email: string) => {
    try {
      await apiClient.post('/auth/password-reset/', {
        email,
      });

      return { error: null };
    } catch (error: any) {
      return {
        error: {
          message: error.response?.data?.error || 'Password reset failed'
        }
      };
    }
  };

  return {
    user,
    session: user ? { user } : null,
    loading,
    signUp,
    signIn,
    signInWithGoogle,
    signInWithFacebook,
    signInWithApple,
    signOut,
    resetPassword,
  };
};
