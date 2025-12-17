import { Toaster } from "@/components/ui/toaster";
import { Toaster as Sonner } from "@/components/ui/sonner";
import { TooltipProvider } from "@/components/ui/tooltip";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { useAuth } from "@/hooks/useAuth";
import { Layout } from "@/components/Layout";
import Auth from "./pages/Auth";
import Index from "./pages/Index";
import DashboardPage from "./pages/DashboardPage";
import Generate from "./pages/Generate";
import MyProjects from "./pages/MyProjects";
import IdeaGenerator from "./pages/IdeaGenerator";
import Templates from "./pages/Templates";
import AITools from "./pages/AITools";
import Settings from "./pages/Settings";
import NotFound from "./pages/NotFound";
import { InstallPrompt } from "./components/InstallPrompt";

const queryClient = new QueryClient();

// Protected route wrapper
const ProtectedRoute = ({ children }: { children: React.ReactNode }) => {
  const { user, loading } = useAuth();
  
  if (loading) return null;
  if (!user) return <Navigate to="/auth" replace />;
  
  return <>{children}</>;
};

function AppRoutes() {
  const { loading } = useAuth();

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-background">
        <div className="text-center">
          <img src="/Icon.png" alt="SyncFloww" className="w-12 h-12 mx-auto mb-4 animate-pulse" />
          <p className="text-muted-foreground">Loading...</p>
        </div>
      </div>
    );
  }

  return (
    <Routes>
      {/* Landing page - shows landing for unauth, dashboard for auth */}
      <Route path="/" element={<Index />} />
      <Route path="/auth" element={<Auth />} />
      
      {/* Protected routes with sidebar layout */}
      <Route element={<ProtectedRoute><Layout /></ProtectedRoute>}>
        <Route path="/dashboard" element={<DashboardPage />} />
        <Route path="/generate" element={<Generate />} />
        <Route path="/my-projects" element={<MyProjects />} />
        <Route path="/idea-generator" element={<IdeaGenerator />} />
        <Route path="/templates" element={<Templates />} />
        <Route path="/ai-tools" element={<AITools />} />
        <Route path="/settings" element={<Settings />} />
        <Route path="/customers" element={<DashboardPage />} />
        <Route path="/calendar" element={<DashboardPage />} />
        <Route path="/analytics" element={<DashboardPage />} />
      </Route>
      
      <Route path="*" element={<NotFound />} />
    </Routes>
  );
}

const App = () => (
  <QueryClientProvider client={queryClient}>
    <TooltipProvider>
      <Toaster />
      <Sonner />
      <BrowserRouter>
        <AppRoutes />
        <InstallPrompt />
      </BrowserRouter>
    </TooltipProvider>
  </QueryClientProvider>
);

export default App;
