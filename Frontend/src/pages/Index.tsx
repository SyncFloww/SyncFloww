import { useNavigate } from 'react-router-dom';
import { useAuth } from '@/hooks/useAuth';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';
import { Label } from '@/components/ui/label';
import DashboardPage from './DashboardPage';
import logoHeaderBlue from '@/assets/logo-header-blue.png';
import { motion, AnimatePresence } from 'framer-motion';
import { useState } from 'react';
import { useToast } from '@/hooks/use-toast';
import { 
  Sparkles, 
  TrendingUp, 
  Video,
  ArrowRight,
  Check,
  HelpCircle,
  Mail,
  Send,
  Quote
} from 'lucide-react';
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar';
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from '@/components/ui/accordion';

const pageTransition = {
  initial: { opacity: 0, y: 20 },
  animate: { opacity: 1, y: 0 },
  exit: { opacity: 0, y: -20 },
  transition: { duration: 0.4, ease: [0.4, 0, 0.2, 1] }
};

const staggerContainer = {
  animate: {
    transition: {
      staggerChildren: 0.1
    }
  }
};

const fadeInUp = {
  initial: { opacity: 0, y: 30 },
  animate: { opacity: 1, y: 0, transition: { duration: 0.5 } }
};

const pricingTiers = [
  {
    name: 'Starter',
    price: 'Free',
    description: 'Perfect for trying out SyncFloww',
    features: [
      '5 AI ideas per month',
      'Basic virality scoring',
      '1 brand profile',
      'Community support'
    ],
    cta: 'Get Started',
    popular: false
  },
  {
    name: 'Pro',
    price: '$29',
    period: '/month',
    description: 'Best for content creators',
    features: [
      'Unlimited AI ideas',
      'Advanced virality scoring',
      '5 brand profiles',
      'Production packages',
      'Priority support',
      'Team collaboration'
    ],
    cta: 'Start Free Trial',
    popular: true
  },
  {
    name: 'Enterprise',
    price: 'Custom',
    description: 'For agencies & large teams',
    features: [
      'Everything in Pro',
      'Unlimited brands',
      'Custom AI training',
      'API access',
      'Dedicated account manager',
      'SSO & advanced security'
    ],
    cta: 'Contact Sales',
    popular: false
  }
];

const testimonials = [
  {
    name: 'Sarah Chen',
    role: 'Content Creator',
    followers: '2.1M followers',
    avatar: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=150&h=150&fit=crop&crop=face',
    quote: 'SyncFloww completely transformed my content strategy. My videos went from 10K to 500K views consistently. The virality scoring is scary accurate!',
    platform: 'TikTok'
  },
  {
    name: 'Marcus Johnson',
    role: 'Social Media Manager',
    followers: 'Agency Owner',
    avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&h=150&fit=crop&crop=face',
    quote: 'Managing 15+ brand accounts became so much easier. The AI agents save us 20+ hours per week on content ideation alone.',
    platform: 'Multi-platform'
  },
  {
    name: 'Emma Rodriguez',
    role: 'Lifestyle Influencer',
    followers: '850K followers',
    avatar: 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=150&h=150&fit=crop&crop=face',
    quote: 'The production packages are a game-changer. I went from spending days on scripts to having everything ready in minutes.',
    platform: 'Instagram'
  }
];

const LandingPage = () => {
  const navigate = useNavigate();
  const { toast } = useToast();
  const [contactForm, setContactForm] = useState({
    name: '',
    email: '',
    message: ''
  });
  const [isSubmitting, setIsSubmitting] = useState(false);

  const scrollToSection = (sectionId: string) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  };

  const handleContactSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSubmitting(true);
    
    // Simulate form submission
    await new Promise(resolve => setTimeout(resolve, 1000));
    
    toast({
      title: 'Message sent!',
      description: 'Thanks for reaching out. We\'ll get back to you within 24 hours.',
    });
    
    setContactForm({ name: '', email: '', message: '' });
    setIsSubmitting(false);
  };

  return (
    <motion.div 
      className="min-h-screen bg-gradient-to-br from-background via-background to-primary/5"
      initial="initial"
      animate="animate"
      exit="exit"
      variants={pageTransition}
    >
      {/* Header */}
      <header className="fixed top-0 left-0 right-0 z-50 bg-background/80 backdrop-blur-md border-b border-border">
        <div className="container mx-auto px-6 h-16 flex items-center justify-between">
          <img src={logoHeaderBlue} alt="SyncFloww" className="h-8" />
          <nav className="hidden md:flex items-center gap-6">
            <button 
              onClick={() => scrollToSection('features')}
              className="text-sm text-muted-foreground hover:text-foreground transition-colors"
            >
              Features
            </button>
            <button 
              onClick={() => scrollToSection('pricing')}
              className="text-sm text-muted-foreground hover:text-foreground transition-colors"
            >
              Pricing
            </button>
            <button 
              onClick={() => scrollToSection('testimonials')}
              className="text-sm text-muted-foreground hover:text-foreground transition-colors"
            >
              Testimonials
            </button>
            <button 
              onClick={() => scrollToSection('faq')}
              className="text-sm text-muted-foreground hover:text-foreground transition-colors"
            >
              FAQ
            </button>
            <button 
              onClick={() => scrollToSection('contact')}
              className="text-sm text-muted-foreground hover:text-foreground transition-colors"
            >
              Contact
            </button>
          </nav>
          <div className="flex items-center gap-4">
            <Button variant="ghost" onClick={() => navigate('/auth')}>
              Log in
            </Button>
            <Button onClick={() => navigate('/auth')}>
              Sign up
            </Button>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <motion.section 
        className="pt-32 pb-20 px-6"
        variants={staggerContainer}
      >
        <div className="container mx-auto text-center">
          <motion.div 
            className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-primary/10 text-primary text-sm font-medium mb-6"
            variants={fadeInUp}
          >
            <Sparkles className="w-4 h-4" />
            AI-Powered Video Pre-Production
          </motion.div>
          <motion.h1 
            className="text-4xl md:text-6xl font-bold text-foreground mb-6 max-w-4xl mx-auto leading-tight"
            variants={fadeInUp}
          >
            Create Viral Short-Form Videos with AI
          </motion.h1>
          <motion.p 
            className="text-lg md:text-xl text-muted-foreground mb-8 max-w-2xl mx-auto"
            variants={fadeInUp}
          >
            Your AI co-pilot for ideation, scripting, and production planning. Turn ideas into viral-ready content in minutes.
          </motion.p>
          <motion.div 
            className="flex flex-col sm:flex-row items-center justify-center gap-4"
            variants={fadeInUp}
          >
            <Button size="lg" onClick={() => navigate('/auth')} className="gap-2">
              Get Started Free
              <ArrowRight className="w-4 h-4" />
            </Button>
            <Button size="lg" variant="outline" onClick={() => navigate('/auth')}>
              Watch Demo
            </Button>
          </motion.div>
        </div>
      </motion.section>

      {/* Features Section */}
      <motion.section 
        id="features"
        className="py-20 px-6 bg-surface/50"
        initial={{ opacity: 0 }}
        whileInView={{ opacity: 1 }}
        viewport={{ once: true }}
        transition={{ duration: 0.6 }}
      >
        <div className="container mx-auto">
          <h2 className="text-3xl font-bold text-center text-foreground mb-12">
            Everything You Need to Go Viral
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {[
              { icon: Sparkles, title: 'AI Idea Generator', desc: 'Generate trending content ideas tailored to your niche, audience, and goals.', color: 'primary' },
              { icon: TrendingUp, title: 'Virality Scoring', desc: 'Get AI-powered predictions on your content\'s viral potential before you create.', color: 'secondary' },
              { icon: Video, title: 'Production Packages', desc: 'Auto-generate scripts, storyboards, and production briefs ready for filming.', color: 'ai' }
            ].map((feature, i) => (
              <motion.div 
                key={feature.title}
                className="p-6 rounded-xl bg-background border border-border hover:shadow-lg transition-all"
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.1, duration: 0.5 }}
                whileHover={{ y: -5 }}
              >
                <div className={`w-12 h-12 rounded-lg bg-${feature.color}/10 flex items-center justify-center mb-4`}>
                  <feature.icon className={`w-6 h-6 text-${feature.color}`} />
                </div>
                <h3 className="text-xl font-semibold text-foreground mb-2">{feature.title}</h3>
                <p className="text-muted-foreground">{feature.desc}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </motion.section>

      {/* Testimonials Section */}
      <motion.section 
        id="testimonials"
        className="py-20 px-6"
        initial={{ opacity: 0 }}
        whileInView={{ opacity: 1 }}
        viewport={{ once: true }}
        transition={{ duration: 0.6 }}
      >
        <div className="container mx-auto">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold text-foreground mb-4">
              Creators Love SyncFloww
            </h2>
            <p className="text-muted-foreground max-w-2xl mx-auto">
              Join thousands of content creators who've transformed their social media presence with AI-powered insights.
            </p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto">
            {testimonials.map((testimonial, i) => (
              <motion.div
                key={testimonial.name}
                className="relative p-6 rounded-2xl bg-background border border-border hover:shadow-lg transition-all"
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.1, duration: 0.5 }}
                whileHover={{ y: -5 }}
              >
                <Quote className="absolute top-4 right-4 w-8 h-8 text-primary/20" />
                <div className="flex items-center gap-4 mb-4">
                  <Avatar className="w-14 h-14 border-2 border-primary/20">
                    <AvatarImage src={testimonial.avatar} alt={testimonial.name} />
                    <AvatarFallback className="bg-primary/10 text-primary font-semibold">
                      {testimonial.name.split(' ').map(n => n[0]).join('')}
                    </AvatarFallback>
                  </Avatar>
                  <div>
                    <h4 className="font-semibold text-foreground">{testimonial.name}</h4>
                    <p className="text-sm text-muted-foreground">{testimonial.role}</p>
                    <p className="text-xs text-primary">{testimonial.followers}</p>
                  </div>
                </div>
                <p className="text-muted-foreground italic leading-relaxed">
                  "{testimonial.quote}"
                </p>
                <div className="mt-4 pt-4 border-t border-border">
                  <span className="text-xs font-medium text-secondary">{testimonial.platform}</span>
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </motion.section>

      {/* Pricing Section */}
      <motion.section 
        id="pricing"
        className="py-20 px-6"
        initial={{ opacity: 0 }}
        whileInView={{ opacity: 1 }}
        viewport={{ once: true }}
        transition={{ duration: 0.6 }}
      >
        <div className="container mx-auto">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold text-foreground mb-4">
              Simple, Transparent Pricing
            </h2>
            <p className="text-muted-foreground max-w-2xl mx-auto">
              Choose the plan that fits your creative workflow. Start free and scale as you grow.
            </p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl mx-auto">
            {pricingTiers.map((tier, i) => (
              <motion.div
                key={tier.name}
                className={`relative p-6 rounded-2xl border ${
                  tier.popular 
                    ? 'border-primary bg-primary/5 shadow-lg shadow-primary/10' 
                    : 'border-border bg-background'
                }`}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.1, duration: 0.5 }}
                whileHover={{ y: -5 }}
              >
                {tier.popular && (
                  <div className="absolute -top-3 left-1/2 -translate-x-1/2 px-3 py-1 bg-primary text-primary-foreground text-xs font-medium rounded-full">
                    Most Popular
                  </div>
                )}
                <div className="text-center mb-6">
                  <h3 className="text-xl font-semibold text-foreground mb-2">{tier.name}</h3>
                  <div className="flex items-baseline justify-center gap-1">
                    <span className="text-4xl font-bold text-foreground">{tier.price}</span>
                    {tier.period && <span className="text-muted-foreground">{tier.period}</span>}
                  </div>
                  <p className="text-sm text-muted-foreground mt-2">{tier.description}</p>
                </div>
                <ul className="space-y-3 mb-6">
                  {tier.features.map((feature) => (
                    <li key={feature} className="flex items-center gap-2 text-sm text-foreground">
                      <Check className="w-4 h-4 text-primary flex-shrink-0" />
                      {feature}
                    </li>
                  ))}
                </ul>
                <Button 
                  className="w-full" 
                  variant={tier.popular ? 'default' : 'outline'}
                  onClick={() => navigate('/auth')}
                >
                  {tier.cta}
                </Button>
              </motion.div>
            ))}
          </div>
        </div>
      </motion.section>

      {/* FAQ Section */}
      <motion.section 
        id="faq"
        className="py-20 px-6 bg-surface/50"
        initial={{ opacity: 0 }}
        whileInView={{ opacity: 1 }}
        viewport={{ once: true }}
        transition={{ duration: 0.6 }}
      >
        <div className="container mx-auto max-w-3xl">
          <div className="text-center mb-12">
            <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-primary/10 text-primary text-sm font-medium mb-4">
              <HelpCircle className="w-4 h-4" />
              FAQ
            </div>
            <h2 className="text-3xl font-bold text-foreground mb-4">
              Frequently Asked Questions
            </h2>
            <p className="text-muted-foreground">
              Got questions? We've got answers. If you can't find what you're looking for, reach out to our support team.
            </p>
          </div>
          
          <Accordion type="single" collapsible className="w-full space-y-4">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: 0.1, duration: 0.5 }}
            >
              <AccordionItem value="item-1" className="border border-border rounded-xl px-6 bg-background">
                <AccordionTrigger className="text-left font-semibold hover:no-underline">
                  How does the AI idea generator work?
                </AccordionTrigger>
                <AccordionContent className="text-muted-foreground">
                  Our AI analyzes trending content across platforms, your niche, target audience, and goals to generate unique, tailored video ideas. It uses the 6-Part Viral Video Formula to ensure each idea has maximum viral potential, scoring elements like hook strength, emotional resonance, and shareability.
                </AccordionContent>
              </AccordionItem>
            </motion.div>
            
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: 0.2, duration: 0.5 }}
            >
              <AccordionItem value="item-2" className="border border-border rounded-xl px-6 bg-background">
                <AccordionTrigger className="text-left font-semibold hover:no-underline">
                  What's included in a production package?
                </AccordionTrigger>
                <AccordionContent className="text-muted-foreground">
                  Each production package includes a detailed script with timing, a visual storyboard, shot-by-shot production brief, suggested music/sound effects, caption variations optimized for each platform, and thumbnail concepts. Everything you need to go from idea to filming in minutes.
                </AccordionContent>
              </AccordionItem>
            </motion.div>
            
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: 0.3, duration: 0.5 }}
            >
              <AccordionItem value="item-3" className="border border-border rounded-xl px-6 bg-background">
                <AccordionTrigger className="text-left font-semibold hover:no-underline">
                  Can I use SyncFloww for multiple brands?
                </AccordionTrigger>
                <AccordionContent className="text-muted-foreground">
                  Yes! Our Pro plan supports up to 5 brand profiles, and Enterprise offers unlimited brands. Each brand profile stores unique voice, tone, audience demographics, and content preferences, ensuring AI-generated ideas stay consistent with each brand's identity.
                </AccordionContent>
              </AccordionItem>
            </motion.div>
            
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: 0.4, duration: 0.5 }}
            >
              <AccordionItem value="item-4" className="border border-border rounded-xl px-6 bg-background">
                <AccordionTrigger className="text-left font-semibold hover:no-underline">
                  How accurate is the virality scoring?
                </AccordionTrigger>
                <AccordionContent className="text-muted-foreground">
                  Our virality scoring is based on analysis of millions of viral videos and the proven 6-Part Viral Video Formula. While no system can guarantee virality, our scoring helps identify and strengthen the key elements that successful viral content consistently shares, significantly improving your odds.
                </AccordionContent>
              </AccordionItem>
            </motion.div>
            
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: 0.5, duration: 0.5 }}
            >
              <AccordionItem value="item-5" className="border border-border rounded-xl px-6 bg-background">
                <AccordionTrigger className="text-left font-semibold hover:no-underline">
                  Is there a free trial available?
                </AccordionTrigger>
                <AccordionContent className="text-muted-foreground">
                  Absolutely! Our Starter plan is completely free and includes 5 AI ideas per month, basic virality scoring, and 1 brand profile. You can upgrade to Pro anytime for unlimited ideas and advanced features. We also offer a 14-day free trial of Pro for new users.
                </AccordionContent>
              </AccordionItem>
            </motion.div>
          </Accordion>
        </div>
      </motion.section>

      {/* Contact Section */}
      <motion.section 
        id="contact"
        className="py-20 px-6"
        initial={{ opacity: 0 }}
        whileInView={{ opacity: 1 }}
        viewport={{ once: true }}
        transition={{ duration: 0.6 }}
      >
        <div className="container mx-auto max-w-2xl">
          <div className="text-center mb-12">
            <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-primary/10 text-primary text-sm font-medium mb-4">
              <Mail className="w-4 h-4" />
              Contact Us
            </div>
            <h2 className="text-3xl font-bold text-foreground mb-4">
              Get in Touch
            </h2>
            <p className="text-muted-foreground">
              Have questions or feedback? We'd love to hear from you. Our team typically responds within 24 hours.
            </p>
          </div>
          
          <motion.form
            onSubmit={handleContactSubmit}
            className="space-y-6 p-8 rounded-2xl border border-border bg-background shadow-sm"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: 0.2, duration: 0.5 }}
          >
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div className="space-y-2">
                <Label htmlFor="contact-name">Name</Label>
                <Input
                  id="contact-name"
                  placeholder="Your name"
                  value={contactForm.name}
                  onChange={(e) => setContactForm({ ...contactForm, name: e.target.value })}
                  required
                />
              </div>
              <div className="space-y-2">
                <Label htmlFor="contact-email">Email</Label>
                <Input
                  id="contact-email"
                  type="email"
                  placeholder="you@example.com"
                  value={contactForm.email}
                  onChange={(e) => setContactForm({ ...contactForm, email: e.target.value })}
                  required
                />
              </div>
            </div>
            <div className="space-y-2">
              <Label htmlFor="contact-message">Message</Label>
              <Textarea
                id="contact-message"
                placeholder="How can we help you?"
                rows={5}
                value={contactForm.message}
                onChange={(e) => setContactForm({ ...contactForm, message: e.target.value })}
                required
              />
            </div>
            <Button type="submit" className="w-full gap-2" disabled={isSubmitting}>
              {isSubmitting ? (
                'Sending...'
              ) : (
                <>
                  Send Message
                  <Send className="w-4 h-4" />
                </>
              )}
            </Button>
          </motion.form>
        </div>
      </motion.section>

      {/* CTA Section */}
      <motion.section 
        className="py-20 px-6 bg-surface/50"
        initial={{ opacity: 0, scale: 0.95 }}
        whileInView={{ opacity: 1, scale: 1 }}
        viewport={{ once: true }}
        transition={{ duration: 0.5 }}
      >
        <div className="container mx-auto text-center">
          <div className="max-w-3xl mx-auto p-8 rounded-2xl bg-gradient-to-r from-primary to-primary/80 text-primary-foreground">
            <h2 className="text-3xl font-bold mb-4">Ready to Create Viral Content?</h2>
            <p className="text-lg opacity-90 mb-6">
              Join thousands of creators using SyncFloww to plan their next viral hit.
            </p>
            <Button size="lg" variant="secondary" onClick={() => navigate('/auth')}>
              Start Creating for Free
            </Button>
          </div>
        </div>
      </motion.section>

      {/* Footer */}
      <footer className="py-8 px-6 border-t border-border">
        <div className="container mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
          <img src={logoHeaderBlue} alt="SyncFloww" className="h-6" />
          <nav className="flex gap-6 text-sm text-muted-foreground">
            <button onClick={() => scrollToSection('features')} className="hover:text-foreground transition-colors">Features</button>
            <button onClick={() => scrollToSection('pricing')} className="hover:text-foreground transition-colors">Pricing</button>
            <button onClick={() => scrollToSection('faq')} className="hover:text-foreground transition-colors">FAQ</button>
            <button onClick={() => scrollToSection('contact')} className="hover:text-foreground transition-colors">Contact</button>
          </nav>
          <p className="text-sm text-muted-foreground">
            © 2024 SyncFloww. All rights reserved.
          </p>
        </div>
      </footer>
    </motion.div>
  );
};

const Index = () => {
  const { user, loading } = useAuth();

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-background">
        <motion.div 
          className="text-center"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
        >
          <img src="/Icon.png" alt="SyncFloww" className="w-12 h-12 mx-auto mb-4 animate-pulse" />
          <p className="text-muted-foreground">Loading...</p>
        </motion.div>
      </div>
    );
  }

  return (
    <AnimatePresence mode="wait">
      {!user ? (
        <LandingPage key="landing" />
      ) : (
        <motion.div
          key="dashboard"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -20 }}
          transition={{ duration: 0.4 }}
        >
          <DashboardPage />
        </motion.div>
      )}
    </AnimatePresence>
  );
};

export default Index;
