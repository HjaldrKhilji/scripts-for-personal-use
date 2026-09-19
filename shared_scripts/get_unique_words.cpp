//while this isnt technically a script, it is as useful to me as a script would conventional be
//the application is just being able to solve slot conflicts in gentoo or atleast being able to get a unique set of USE flags
#include<iostream>
#include<string>
#include<vector>
#include<flat_set>
namespace read_from_commandline{
	std::flat_set<std::string_view> read(int argc, char *argv[]);
	namespace read_options{
		std::string_view read_args(std::string_view src){
			return src.subview(0, src.find_first_of(' '));
		}
		enum class command_line_option{
	        remove_if_any_prefix=0;
  	     	};
		struct options_and_option_args{
		command_line_options option;
		std::string_view argument;
		};
		using input_ops=std::vector<options_and_option_args>;
		input_ops read(std::string_view options);
		input_ops read_impl(command_line_options option, std::string_view options){
                std::string_view args=read_args( options.subview( options.find_first_of(' ') )  );
		result.push_back(option, args);
                more_options=read(options);
		result.insert_ranges(std::back_inserter(result), more_options);
		return result;
		}
		input_ops read(std::string_view options){
		switch(option[0]){
                case 'r':
			return read_impl(command_line_option::remove_if_any_prefix, options);
                default:
                        std::println(std::cerr, "invalid option '{}' specified", option[0]);
                }
       		}

	};
	std::flat_set<std::string_view> read_unique(int argc, char *argv[]){
                std::flat_set<std::string_view> words{};
                for(int i=0; i<argc; i++){
                        auto elem_to_add=std::string_view{argv[i]};
                        if(!words.contains(elem_to_add)){
                                words.insert(argv[i]);
                        }
                }
                return words;
        }
	std::flat_set<std::string_view> read_unique_and_remove_some(int argc, char *argv[], std::string_view prefix){
    		std::flat_set<std::string_view> words{};
        	for(int i=0; i<argc; i++){
            		auto elem_to_add=std::string_view{argv[i]};
			auto pos=elem_to_add.find_first_of(prefix);
            		if(
			!words.contains(elem_to_add) && !(	pos==0 && words.contains(elem_to_add.subview(pos))	)
			){
                		words.insert(argv[i]);
            		}
        	}
    		return words;
	}
	std::flat_set<std::string_view> read(int argc, char *argv[]){
		std::flat_set<std::string_view> words{};
		if(argc<2){
		std::println(std::cerr, "Too few arguments passed");
		}
		std::string_view options{argv[0]};
		if(options[0]]=='-'){
			if(options[1]==' '){
				std::println(std::cerr, "no option specified after '-'");
			}
			else{
				read(options.subview(1))
			}
		}
		else{
			read_unique(argc-1, argv+1);
		}
	}
};
int main(int argc, char *argv[]){

return 0;
}
