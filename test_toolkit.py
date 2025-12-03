import sys
import os
from datetime import datetime


class ToolkitValidator:
    
    def __init__(self):
        self.passed = []
        self.failed = []
        self.warnings = []
    
    def log_pass(self, test_name: str):
        self.passed.append(test_name)
        print(f"✓ {test_name}")
    
    def log_fail(self, test_name: str, error: str):
        self.failed.append((test_name, error))
        print(f"✗ {test_name}: {error}")
    
    def log_warning(self, test_name: str, message: str):
        self.warnings.append((test_name, message))
        print(f"⚠ {test_name}: {message}")
    
    def test_dependencies(self):
        print("\n" + "="*70)
        print("Testing Dependencies")
        print("="*70)
        
        required = [
            'pandas', 'numpy', 'plotly', 'scipy', 
            'sklearn', 'requests', 'pyarrow'
        ]
        
        for package in required:
            try:
                __import__(package)
                self.log_pass(f"Package {package}")
            except ImportError as e:
                self.log_fail(f"Package {package}", str(e))
    
    def test_file_structure(self):
        print("\n" + "="*70)
        print("Testing File Structure")
        print("="*70)
        
        required_files = [
            'worldbank_toolkit/__init__.py',
            'worldbank_toolkit/base_connector.py',
            'worldbank_toolkit/data_harmonizer.py',
            'worldbank_toolkit/category_analyzers.py',
            'worldbank_toolkit/advanced_analyzers.py',
            'worldbank_toolkit/visualizer.py',
            'worldbank_challenge_orchestrator.py',
            'presentation_generator.py',
            'requirements.txt',
            'README_WORLDBANK.md',
            'EXECUTION_CHECKLIST.md',
            'WORLD_BANK_CHALLENGE_META_ANALYSIS.md'
        ]
        
        for filepath in required_files:
            if os.path.exists(filepath):
                self.log_pass(f"File {filepath}")
            else:
                self.log_fail(f"File {filepath}", "File not found")
    
    def test_imports(self):
        print("\n" + "="*70)
        print("Testing Module Imports")
        print("="*70)
        
        try:
            from worldbank_toolkit import (
                WorldBankConnector, ILOConnector, UNSDGConnector,
                DataHarmonizer, BusinessEnvironmentAnalyzer,
                GenderAnalyzer, YouthAnalyzer, PublicPrivateNexusAnalyzer,
                FrontierTrendsAnalyzer, WorldBankVisualizer
            )
            self.log_pass("WorldBank Toolkit imports")
        except ImportError as e:
            self.log_fail("WorldBank Toolkit imports", str(e))
        
        try:
            from worldbank_challenge_orchestrator import WorldBankChallengeOrchestrator
            self.log_pass("Orchestrator import")
        except ImportError as e:
            self.log_fail("Orchestrator import", str(e))
        
        try:
            from presentation_generator import PresentationGenerator
            self.log_pass("Presentation Generator import")
        except ImportError as e:
            self.log_fail("Presentation Generator import", str(e))
    
    def test_connector_initialization(self):
        print("\n" + "="*70)
        print("Testing Connector Initialization")
        print("="*70)
        
        try:
            from worldbank_toolkit import WorldBankConnector
            connector = WorldBankConnector(cache_dir='./test_cache')
            self.log_pass("WorldBankConnector initialization")
        except Exception as e:
            self.log_fail("WorldBankConnector initialization", str(e))
        
        try:
            from worldbank_toolkit import ILOConnector
            connector = ILOConnector(cache_dir='./test_cache')
            self.log_pass("ILOConnector initialization")
        except Exception as e:
            self.log_fail("ILOConnector initialization", str(e))
        
        try:
            from worldbank_toolkit import UNSDGConnector
            connector = UNSDGConnector(cache_dir='./test_cache')
            self.log_pass("UNSDGConnector initialization")
        except Exception as e:
            self.log_fail("UNSDGConnector initialization", str(e))
    
    def test_analyzer_initialization(self):
        print("\n" + "="*70)
        print("Testing Analyzer Initialization")
        print("="*70)
        
        import pandas as pd
        
        sample_data = pd.DataFrame({
            'country_code': ['USA', 'GBR', 'DEU'],
            'year': [2020, 2020, 2020],
            'gdp_growth': [2.3, 1.5, 1.8]
        })
        
        analyzers = [
            ('BusinessEnvironmentAnalyzer', 'BusinessEnvironmentAnalyzer'),
            ('GenderAnalyzer', 'GenderAnalyzer'),
            ('YouthAnalyzer', 'YouthAnalyzer'),
            ('PublicPrivateNexusAnalyzer', 'PublicPrivateNexusAnalyzer'),
            ('FrontierTrendsAnalyzer', 'FrontierTrendsAnalyzer')
        ]
        
        for name, class_name in analyzers:
            try:
                from worldbank_toolkit import category_analyzers, advanced_analyzers
                
                if hasattr(category_analyzers, class_name):
                    analyzer_class = getattr(category_analyzers, class_name)
                else:
                    analyzer_class = getattr(advanced_analyzers, class_name)
                
                analyzer = analyzer_class(sample_data)
                self.log_pass(f"{name} initialization")
            except Exception as e:
                self.log_fail(f"{name} initialization", str(e))
    
    def test_visualizer(self):
        print("\n" + "="*70)
        print("Testing Visualizer")
        print("="*70)
        
        try:
            from worldbank_toolkit import WorldBankVisualizer
            import pandas as pd
            
            visualizer = WorldBankVisualizer()
            self.log_pass("Visualizer initialization")
            
            sample_data = pd.DataFrame({
                'country_code': ['USA', 'GBR', 'DEU'],
                'country_name': ['United States', 'United Kingdom', 'Germany'],
                'value': [10, 20, 15]
            })
            
            fig = visualizer.create_bar_chart_ranking(
                sample_data, 'country_code', 'value',
                'Test Chart', top_n=3
            )
            
            self.log_pass("Visualizer chart creation")
            
        except Exception as e:
            self.log_fail("Visualizer functionality", str(e))
    
    def test_orchestrator_sample_run(self):
        print("\n" + "="*70)
        print("Testing Orchestrator (Sample Data)")
        print("="*70)
        
        try:
            from worldbank_challenge_orchestrator import WorldBankChallengeOrchestrator
            import pandas as pd
            
            orchestrator = WorldBankChallengeOrchestrator(
                cache_dir='./test_cache',
                output_dir='./test_results'
            )
            
            self.log_pass("Orchestrator initialization")
            
            sample_data = orchestrator._generate_sample_data()
            
            if 'unified' in sample_data and not sample_data['unified'].empty:
                self.log_pass("Sample data generation")
            else:
                self.log_fail("Sample data generation", "Empty DataFrame")
            
        except Exception as e:
            self.log_fail("Orchestrator functionality", str(e))
    
    def test_directory_creation(self):
        print("\n" + "="*70)
        print("Testing Directory Creation")
        print("="*70)
        
        test_dirs = ['./test_cache', './test_results', './test_visualizations']
        
        for directory in test_dirs:
            try:
                os.makedirs(directory, exist_ok=True)
                if os.path.exists(directory):
                    self.log_pass(f"Directory creation: {directory}")
                else:
                    self.log_fail(f"Directory creation: {directory}", "Not created")
            except Exception as e:
                self.log_fail(f"Directory creation: {directory}", str(e))
    
    def cleanup_test_artifacts(self):
        print("\n" + "="*70)
        print("Cleaning Up Test Artifacts")
        print("="*70)
        
        import shutil
        
        test_dirs = ['./test_cache', './test_results', './test_visualizations']
        
        for directory in test_dirs:
            try:
                if os.path.exists(directory):
                    shutil.rmtree(directory)
                    self.log_pass(f"Cleanup: {directory}")
            except Exception as e:
                self.log_warning(f"Cleanup: {directory}", str(e))
    
    def generate_report(self):
        print("\n" + "="*70)
        print("VALIDATION REPORT")
        print("="*70)
        
        total = len(self.passed) + len(self.failed)
        pass_rate = (len(self.passed) / total * 100) if total > 0 else 0
        
        print(f"\nTotal Tests: {total}")
        print(f"Passed: {len(self.passed)} ({pass_rate:.1f}%)")
        print(f"Failed: {len(self.failed)}")
        print(f"Warnings: {len(self.warnings)}")
        
        if self.failed:
            print("\n" + "="*70)
            print("FAILED TESTS")
            print("="*70)
            for test_name, error in self.failed:
                print(f"\n✗ {test_name}")
                print(f"  Error: {error}")
        
        if self.warnings:
            print("\n" + "="*70)
            print("WARNINGS")
            print("="*70)
            for test_name, message in self.warnings:
                print(f"\n⚠ {test_name}")
                print(f"  Message: {message}")
        
        print("\n" + "="*70)
        
        if pass_rate >= 90:
            print("✓ TOOLKIT READY FOR DEPLOYMENT")
            print("="*70)
            return 0
        elif pass_rate >= 70:
            print("⚠ TOOLKIT MOSTLY READY - Review failed tests")
            print("="*70)
            return 1
        else:
            print("✗ TOOLKIT NOT READY - Fix critical issues")
            print("="*70)
            return 2
    
    def run_all_tests(self):
        print("\n" + "="*70)
        print("WORLD BANK CHALLENGE TOOLKIT - VALIDATION SUITE")
        print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*70)
        
        self.test_file_structure()
        self.test_dependencies()
        self.test_imports()
        self.test_directory_creation()
        self.test_connector_initialization()
        self.test_analyzer_initialization()
        self.test_visualizer()
        self.test_orchestrator_sample_run()
        self.cleanup_test_artifacts()
        
        return self.generate_report()


def main():
    validator = ToolkitValidator()
    exit_code = validator.run_all_tests()
    
    print("\nNext Steps:")
    if exit_code == 0:
        print("1. Review README_WORLDBANK.md")
        print("2. Check EXECUTION_CHECKLIST.md")
        print("3. Run full pipeline: python worldbank_challenge_orchestrator.py")
        print("4. You're ready for the challenge! 🚀")
    else:
        print("1. Fix failed tests")
        print("2. Install missing dependencies: pip install -r requirements.txt")
        print("3. Re-run validation: python test_toolkit.py")
    
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
