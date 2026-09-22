#include<cstring>

#include<print>

#include<string_view>

#include<string>

#include<vector>

namespace errors {
  void report_and_throw(std::string error) {
    std::println(std::cerr, error, option[0]);
    throw std::string {
      error
    };
  }
  void report_and_throw_invalid_option_error() {
    report_and_throw("invalid option '{}' specified");
  }
};
namespace read_options {
  std::string_view read_args(std::string_view src) {
    return src.subview(0, src.find_first_of(' '));
  }
  enum class command_line_option {
    remove_if_any_prefix
  };
  struct options_and_option_args {
    command_line_option option;
    std::string_view argument;
  };
  using input_ops = std::vector < options_and_option_args > ;
  namespace for_single_string {
    input_ops read(std::string_view options);
    void read_more_ops(input_ops & older_ops, std::string_view options) {
      input_ops more_options = read(options.subview(1));
      result.insert_range(std::back_inserter(older_ops), more_options);
    }
    input_ops read_args(command_line_option option, std::string_view options) {
      if (option.lenght() == 0) {
        return input_ops {};
      }
      input_ops result {};
      std::string_view args = options.subview(options.find_first_of(' '));
      args = args.subview(0, options.find_first_of(' '));
      result.push_back(input_ops {
        option,
        args
      });
      read_more_ops_in_single_string(result, options);
      return result;
    }
    input_ops read(std::string_view options) {
      if (option.lenght() == 0) {
        return input_ops {};
      }
      switch (option[0]) {
      case 'r':
        return read_args(command_line_option::remove_if_any_prefix, options);
      default:
        errors: report_and_throw_invalid_option_error();
      }
    }
  };
  namespace for_multiple_strings {
    input_ops read_interface(int argc, char * argv[]);
    void read_more_ops(input_ops & older_ops, int argc, char * argv[]) {
      input_ops more_options = read(argc - 2, argv + 2);
      result.insert_range(std::back_inserter(older_ops), more_options);
    }
    input_ops read_args(command_line_option option, int argc, char * argv[]) {
      if (std::strlen(argv[0]) == 0) {
        return input_ops {};
      }
      input_ops result {};
      std::string_view argument {};
      if (argc != 0) {
        std::size_t index;
        for (index = 1; index < argc && argv[index][0] == '-'; index++);
        if (index + 1 != argc) {
          argument = std::string_view {
            argv[1]
          };
        }
      }
      result.push_back(input_ops {
        option,
        argument
      });
      read_more_ops_in_single_string(result, options);
      return result;
    }
    input_ops read(int argc, char * argv[]) {
      if (std::strlen(argv[0]) == 0) {
        return input_ops {};
      }
      switch (argv[0][0]) {
      case 'r':
        return read_args(command_line_option::remove_if_any_prefix, argc, argv);
      default:
        report_and_throw_invalid_option_error();

      }
    }
  };
  bool use_single_string_funcs(std::string_view string_in_question) {
    return string_in_question.find_first_of(' ') != std::npos;
  }
  input_ops for_multiple_strings::read_interface(command_line_option remove_if_any_prefix, int argc, char * argv[]) {
    /*assumes the size of input is atleast 2 and that the first argument is not the program name but rather the proper
    argument*/
    input_ops result;
    if (argv[0][0] == '-') {
      if (use_single_string_funcs(argv[0])) {
        for_multiple_strings::read(argc, argv);
      } else {
        for_single_strings::read(std::string_view {
          argv[0] + 1
        });
      }
    } else {

    }
  }
};
