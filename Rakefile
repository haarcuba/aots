desc "delete all *.pyc (compiled python) files"
task :rm_pyc do
    compiledPythons = FileList[ 'jones/**/*.pyc' ]
    puts "DELETE .pyc: will delete #{compiledPythons.count} pyc files"
    compiledPythons.each do |file|
        File.delete( file )
    end
end

tests = FileList[ 'test/**/test*.py' ]
puts "found #{tests.count} test files"
tests.each do |test|
    desc "run tests in #{test}"
    task test do
        sh "pytest -x #{test}"
    end
end

desc "run all tests"
task :test => [ :rm_pyc ] + tests

file '.git/hooks/pre-commit' do
    sh "ln -s ../../tools/pre-commit .git/hooks"
end

desc "setup git commit hook"
task :hooks => '.git/hooks/pre-commit'
