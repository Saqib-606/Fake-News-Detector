# Class To Store NewsArticle Data
class NewsArticle : 
    def __init__(self, title, full_content, source_name, publish_date, author) : # Constructor
        self.title = title
        self.full_content = full_content
        self.source_name = source_name
        self.publish_date = publish_date
        self.author = author


# --------------------------------------------
# Source Credibility Checker
# --------------------------------------------
class Source :
    # Class Variables 
    trusted_sources = {"BBC", "Reuters", "Associated Press (AP)", "Al Jazeera", "The Guardian", "The New York Times", "Washington Post", "Bloomberg", "Financial Times", "CNN", "Dawn", "The Express Tribune", "Geo News", "ARY News", "Pakistan Today", "Business Recorder"}

    trusted_sources_score = 80

    neutral_sources = {"Fox News", "Daily Mail", "NY Post", "Independent blogs", "Medium articles", "Personal YouTube", "Facebook page"}

    neutral_sources_score = 50 

    blacklisted_sources = {"BeforeItsNews", "InfoWars", "NaturalNews", "WorldTruth.TV", "The Onion", "Clickbait WordPrees blogs", "news-update-now.xyz", "Random Telegram"}

    blacklisted_sources_score = 20

    unknown_sources_score = 35 # Maybe Real, Maybe Fake


# --------------------------------------------
# Keyword Analysis Engine
# --------------------------------------------
class KeywordEngine : 
    # Composition: KeywordEngine Uses NewsArticle
    def __init__(self, NewsArticle) : 
        self.news = NewsArticle  
        
        # Keywords Sets
        self.click_bait_keywords = {"Shocking", "Unbelievable", "You won't believe", "Must Read", "Goes Viral", "Exposed", "Secret Revaled", "Media won't show", "Banned video", "Truth Finnaly out"} # Set

        self.conspiracy_keywords = {"Hidden Agenda", "Deep State", "Elite Control", "Global Plan", "Mind Control", "Fake Pandemic", "Hoax Exposed"}

        self.urgency_keywords = {"Share before delete", "Forward to everyone", "Don't trust media", "They are lying", "Open your eyes"}    

    def analyzeKeywords (self) : # Method To Analyze Keywords
        suspicious_keyword_score = 0
        found_keywords = []

        # Combine title + full_content
        text = self.news.title + " " + self.news.full_content # Attributes of NewsArticle Class

        # Check clickbait keywords
        for keyword in self.click_bait_keywords :
            if keyword in text :
                suspicious_keyword_score += 1
                found_keywords.append (keyword)

        # Check conspiracy keywords    
        for keyword in self.conspiracy_keywords :
            if keyword in text :
                suspicious_keyword_score += 1
                found_keywords.append (keyword)

        # Check urgency keywrods
        for keyword in self.urgency_keywords :
            if keyword in text :
                suspicious_keyword_score += 1
                found_keywords.append (keyword)

        return { 
            "score" : suspicious_keyword_score,
            "keywords_found" : found_keywords
        }


# --------------------------------------------
# Sensational Content Detector
# --------------------------------------------
class SensationDetector :
    def __init__(self, NewsArticle) :
        self.news = NewsArticle

        self.indicators = ["This will change your life", "Everyone is scared", "People are angry", "Nation Shocked", "Breaking Shocking News", "Unbelievable Incident"] # Clear Signal

        self.fear = ["Fear", "Panic", "Scared", "Terrified", "Terror", "Danger", "Threat", "Emergency", "Alarming", "Frightening", "Nightmare"]

        self.anger = ["Angry", "Rage", "Outrage", "Furious", "Hate", "Betrayal", "Corrupt", "Criminal", "Liars", "Traitors", "Disgusting"]

        self.shock = ["Shocking", "Unbelievable", "Horrifying", "Explosive", "Bombsheel", "Disturbing", "Unexpected", "Jaw-dropping", "Unthinkable"]

        self.all_caps_detected = False

        self.excessive_punctuation_detected = False

        self.emotional_language_detected = False


    def analyzeSensation (self) :
        sensation_score = 0

        text = self.news.title + " " + self.news.full_content

        # Indicators
        for keywords in self.indicators :
            if keywords in text :
                sensation_score += 1
            
        # Excessive Puncation
        if text.count ("!") >= 5 or text.count ("?") >= 5 or text.count ("!!") >= 5 or text.count ("!?") >= 5 or text.count ("?!") >= 5 :
            self.excessive_punctuation_detected = True
            sensation_score += 1     
       
        # Emotional Language        
        for word in self.fear + self.anger + self.shock :
            if word in text :
                self.emotional_language_detected = True
                sensation_score += 1
                break
        
        # Excessive Caps Lock
        words = text.split ()
        caps_words = 0

        for word in words :
            if word.isupper () and len (word) > 2 : 
                caps_words += 1

        if len (words) > 0 and (caps_words / len (words)) > 0.3 :
            self.all_caps_detected = True
            sensation_score += 1
        
        # return sensation_score
        return {
            "Sensation_score" : sensation_score,
            "Excessive Punctuation": self.excessive_punctuation_detected,
            "Emotional Language": self.emotional_language_detected,
            "All Caps" : self.all_caps_detected
        }


# --------------------------------------------
# Text Quality Analyzer
# --------------------------------------------
class TextAnalyzer () :
    def __init__(self, NewsArticle, keywordEngine, SensationDector) :
        self.news = NewsArticle           
        self.keyword = keywordEngine      
        self.sensation = SensationDector  

    def analyzeText (self) :
        final_score = 100
        issues = []

        # keyword Analysis
        keyword_report = self.keyword.analyzeKeywords ()

        if keyword_report ["score"] > 0 :
            issues.append ("Suspicious or clickbait-style keywords detected.")
            final_score -= keyword_report ["score"] * 5

        # Sensation Analysis
        sensation_report = self.sensation.analyzeSensation ()

        if sensation_report ["Emotional Language"] :
            issues.append ("Emotional language detected that may be intended to manipulate readers.")
            final_score -= 10

        if sensation_report ["Excessive Punctuation"] :
            issues.append ("Excessive punctuation suggests sensationalism.")
            final_score -= 5

        if sensation_report ["All Caps"] :
            issues.append ("Overuse of capital letters detected.")
            final_score -= 5

        # Structure / Content Checks
        content_length = len (self.news.full_content.split())

        if content_length < 50 :
            issues.append ("Content is too short to be considered credible.")
            final_score -= 10

        if len (self.news.title.split()) > 20 :
            issues.append ("Title appears excessively long or exaggerated.")
            final_score -= 5

        # Score Safety
        if final_score < 0 :
            final_score = 0

        return {
            "Final Score" : final_score,
            "Issues" : issues,
            "Keyword Analysis" : keyword_report,
            "Sensation Analysis" : sensation_report
        }


# --------------------------------------------
# Final Credibility Decision Engine
# --------------------------------------------
class CredibilityEngine () :
    def __init__(self, NewsArticle, TextAnalyzer) :
        self.news = NewsArticle   
        self.text = TextAnalyzer  

    def getSourceScore (self) :
        src = self.news.source_name

        if src in Source.trusted_sources :
            return Source.trusted_sources_score, "Trusted Sources"
        elif src in Source.neutral_sources :
            return Source.neutral_sources_score, "Neutral Sources"
        elif src in Source.blacklisted_sources :
            return Source.blacklisted_sources_score, "Blacklisted Sources"
        else :
            return Source.unknown_sources_score, "Unknown Sources"
    
    def makeDecision (self) :
        explanation = []

        # Source Analysis
        source_score, source_msg = self.getSourceScore ()
        explanation.append (f"Source Check: {source_msg}")

        # Text Analysis
        text_report = self.text.analyzeText ()
        text_score = text_report ["Final Score"]

        explanation.extend (text_report ["Issues"])

        # Final Score
        final_score = (source_score + text_score) // 2  
       
        # Verdict
        if final_score >= 70 :
            verdict = "Likely Real News ✅"
            
        elif final_score >= 40 :
            verdict = "Suspicious Content ⚠️"
        else :
            verdict =  "Likely Fake News ❌"

        return {
            "Final Score" : final_score,
            "Verdict" : verdict,
            "Explanation" : explanation
        }
    
# ============================================
# Program Execution
# ============================================

print("\n" + "=" * 50)
print("        FAKE NEWS DETECTOR SYSTEM")
print("=" * 50)

while True :
    title = input ("\nEnter Title:")
    full_content = input ("Enter Full Content:")
    source_name = input ("Enter Source:")
    publish_date = input ("Enter Publish Date:")
    author = input ("Enter Author:")

    # Creating Objects or Instances of Classes
    news = NewsArticle (title, full_content, source_name, publish_date, author)
    keyword_engine = KeywordEngine (news)
    sensation_detector = SensationDetector (news)
    text_analyzer = TextAnalyzer (news, keyword_engine, sensation_detector)
    credibility_engine = CredibilityEngine (news, text_analyzer)
    news_authenticity = credibility_engine.makeDecision ()

    # Final Output
    print("\n" + "-" * 45)
    print("FINAL ANALYSIS RESULT")
    print("-" * 45)
    print(f"Final Credibility Score : {news_authenticity ['Final Score']}")
    print(f"Verdict               : {news_authenticity ['Verdict']}")
    print("\nKey Observations:")
    for issue in news_authenticity ["Explanation"]:
        print(" -", issue)
    
    another_option = input ("\nWould you like to analyze another news article? (y/n):").lower ()

    if another_option != 'y' :
        print ("\nThank you for using the Fake News Detector. Goodbye! 👋")
        break