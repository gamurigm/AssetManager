type LogLevel = 'info' | 'warn' | 'error' | 'success';

class Logger {
    private isProd = process.env.NODE_ENV === 'production';

    private formatMessage(module: string, message: string) {
        const timestamp = new Date().toLocaleTimeString();
        return `[${timestamp}] [${module.toUpperCase()}] ${message}`;
    }

    info(module: string, message: string, data?: any) {
        console.log(`%c${this.formatMessage(module, message)}`, 'color: #3b82f6', data || '');
    }

    success(module: string, message: string, data?: any) {
        console.log(`%c${this.formatMessage(module, message)}`, 'color: #10b981', data || '');
    }

    warn(module: string, message: string, data?: any) {
        console.warn(`%c${this.formatMessage(module, message)}`, 'color: #f59e0b', data || '');
    }

    error(module: string, message: string, data?: any) {
        console.error(`%c${this.formatMessage(module, message)}`, 'color: #ef4444', data || '');
    }
}

export const logger = new Logger();
