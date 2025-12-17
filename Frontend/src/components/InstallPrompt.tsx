import { useState, useEffect } from 'react';
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from '@/components/ui/dialog';
import { Button } from '@/components/ui/button';
import { Smartphone, Download, X } from 'lucide-react';

interface BeforeInstallPromptEvent extends Event {
  readonly platforms: string[];
  readonly userChoice: Promise<{
    outcome: 'accepted' | 'dismissed';
    platform: string;
  }>;
  prompt(): Promise<void>;
}

export function InstallPrompt() {
  const [showPrompt, setShowPrompt] = useState(false);
  const [deferredPrompt, setDeferredPrompt] = useState<BeforeInstallPromptEvent | null>(null);
  const [isIOS, setIsIOS] = useState(false);
  const [isStandalone, setIsStandalone] = useState(false);

  useEffect(() => {
    // Check if already installed
    const standalone = window.matchMedia('(display-mode: standalone)').matches;
    setIsStandalone(standalone);

    // Check if iOS
    const iOS = /iPad|iPhone|iPod/.test(navigator.userAgent);
    setIsIOS(iOS);

    // Check if already dismissed
    const dismissed = localStorage.getItem('pwa-install-dismissed');
    const dismissedTime = dismissed ? parseInt(dismissed) : 0;
    const oneWeek = 7 * 24 * 60 * 60 * 1000;
    
    if (standalone || (dismissedTime && Date.now() - dismissedTime < oneWeek)) {
      return;
    }

    // Listen for beforeinstallprompt event
    const handleBeforeInstallPrompt = (e: Event) => {
      e.preventDefault();
      setDeferredPrompt(e as BeforeInstallPromptEvent);
      // Show prompt after a short delay
      setTimeout(() => setShowPrompt(true), 2000);
    };

    window.addEventListener('beforeinstallprompt', handleBeforeInstallPrompt);

    // For iOS, show prompt if not standalone
    if (iOS && !standalone) {
      setTimeout(() => setShowPrompt(true), 2000);
    }

    return () => {
      window.removeEventListener('beforeinstallprompt', handleBeforeInstallPrompt);
    };
  }, []);

  const handleInstall = async () => {
    if (deferredPrompt) {
      await deferredPrompt.prompt();
      const { outcome } = await deferredPrompt.userChoice;
      if (outcome === 'accepted') {
        setShowPrompt(false);
      }
      setDeferredPrompt(null);
    }
  };

  const handleDismiss = () => {
    setShowPrompt(false);
    localStorage.setItem('pwa-install-dismissed', Date.now().toString());
  };

  if (isStandalone) return null;

  return (
    <Dialog open={showPrompt} onOpenChange={setShowPrompt}>
      <DialogContent className="max-w-md">
        <DialogHeader>
          <div className="flex justify-center mb-4">
            <div className="w-16 h-16 rounded-2xl bg-gradient-primary flex items-center justify-center shadow-lg">
              <img src="/Icon.png" alt="SyncFloww" className="w-12 h-12" />
            </div>
          </div>
          <DialogTitle className="text-center text-xl">Install SyncFloww</DialogTitle>
          <DialogDescription className="text-center">
            Get the full app experience! Install SyncFloww on your device for faster access and offline features.
          </DialogDescription>
        </DialogHeader>

        <div className="space-y-4 py-4">
          {isIOS ? (
            <div className="bg-muted p-4 rounded-lg">
              <p className="text-sm text-muted-foreground mb-3">To install on iOS:</p>
              <ol className="text-sm space-y-2 text-foreground">
                <li className="flex items-center gap-2">
                  <span className="w-5 h-5 rounded-full bg-primary text-primary-foreground flex items-center justify-center text-xs">1</span>
                  Tap the Share button in Safari
                </li>
                <li className="flex items-center gap-2">
                  <span className="w-5 h-5 rounded-full bg-primary text-primary-foreground flex items-center justify-center text-xs">2</span>
                  Scroll down and tap "Add to Home Screen"
                </li>
                <li className="flex items-center gap-2">
                  <span className="w-5 h-5 rounded-full bg-primary text-primary-foreground flex items-center justify-center text-xs">3</span>
                  Tap "Add" to confirm
                </li>
              </ol>
            </div>
          ) : (
            <div className="flex flex-col gap-3">
              <div className="flex items-center gap-3 p-3 bg-muted rounded-lg">
                <Smartphone className="w-8 h-8 text-primary" />
                <div>
                  <p className="font-medium text-foreground">Quick Access</p>
                  <p className="text-sm text-muted-foreground">Launch directly from your home screen</p>
                </div>
              </div>
              <div className="flex items-center gap-3 p-3 bg-muted rounded-lg">
                <Download className="w-8 h-8 text-primary" />
                <div>
                  <p className="font-medium text-foreground">Works Offline</p>
                  <p className="text-sm text-muted-foreground">Access your projects anywhere</p>
                </div>
              </div>
            </div>
          )}
        </div>

        <div className="flex gap-3">
          <Button variant="outline" className="flex-1" onClick={handleDismiss}>
            <X className="w-4 h-4 mr-2" />
            Not Now
          </Button>
          {!isIOS && deferredPrompt && (
            <Button className="flex-1" onClick={handleInstall}>
              <Download className="w-4 h-4 mr-2" />
              Install App
            </Button>
          )}
          {isIOS && (
            <Button className="flex-1" onClick={handleDismiss}>
              Got it!
            </Button>
          )}
        </div>
      </DialogContent>
    </Dialog>
  );
}
